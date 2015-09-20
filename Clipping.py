def parserecord(recordinfo):
    """parse the type and page or position of a record"""
    # TODO
    return(recordinfo, recordinfo, recordinfo)

def parsetime(timeinfo):
    """get time from a string written in some languages"""
    # For example: 作成日: 2014年10月15日水曜日 14:43:29
    # Another example Hinzugefügt am Freitag, 23. Januar 2015 09:30:51
    # TODO
    return(timeinfo)

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
        self.timeinfo = infos[-1]

        #type and page or position
        self.type, self.page, self.location = parserecord(self.recordinfo)

        # date & time
        self.dateTimeAdded = parsetime(self.timeinfo)
        
        self.content = chunkLines[2:]
