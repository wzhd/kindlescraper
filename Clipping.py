import re
import datetime
import locale

def parserecord(recordinfo):
    """parse the type and page or position of a record"""
    # TODO
    return(recordinfo, recordinfo, recordinfo)

def parsetime(timeinfo):
    """get time from a string written in some languages"""
    # For example: 作成日: 2014年10月15日水曜日 14:43:29
    # Another example Hinzugefügt am Freitag, 23. Januar 2015 09:30:51
    # To get month names easily, use locales.
    # Capture the date in a group, time in another group.
    timeformats = [
        ('ja_JP.UTF-8',
         r'作成日: ([0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日)[日月火水木金土]曜日 ([0-9]{1,2}:[0-9]{2}:[0-9]{2})',
         '%Y年%m月%d日 %H:%M:%S'),
        ('de_DE.UTF-8',
         r'Hinzugefügt am \w{6,10}, ([0-9]{1,2}. \w{3,9} [0-9]{4}) ([0-9]{2}:[0-9]{2}:[0-9]{2})',
         # %B is locale’s full month name.
         '%d. %B %Y %H:%M:%S'),
    ]
    date = None
    for timeformat in timeformats:
        m = re.match(timeformat[1], timeinfo)
        if m != None and len(m.groups()) == 2:
            locale.setlocale(locale.LC_TIME,timeformat[0])
            date = datetime.datetime.strptime(' '.join(m.groups()), timeformat[2])
            break
    if date == None:
        raise ValueError('Failed to parse the time')
    return(date)

class Clipping:
    
    type = ""
    title = ""
    page = 0
    location = 0
    recordinfo = None
    timeinfo = None
    dateTimeAdded = ""
    content = ""
    
    def __init__(self, chunk):
        chunkLines = chunk.split('\n')
        chunkLines =[l.strip() for l in chunkLines if len(l) > 0]

        #title
        self.title = chunkLines[0]

        infoLine = chunkLines[1]

        # Perhaps the format changed. The separator is "|" now.
        infos = infoLine.split("|")
        # Usually there is only one "|" in a line, but sometimes ther are two.
        # Such as "- Ihre Notiz auf Seite 17 | bei Position 270 | Hinzugefügt..."
        self.recordinfo = ''.join(infos[:-1])
        self.timeinfo = infos[-1].strip()

        #type and page or position
        self.type, self.page, self.location = parserecord(self.recordinfo)

        # date & time
        self.dateTimeAdded = parsetime(self.timeinfo)
        
        self.content = chunkLines[2:]
