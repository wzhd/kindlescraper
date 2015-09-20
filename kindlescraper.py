import argparse
from Clipping import Clipping

p = argparse.ArgumentParser(description='scrap kindle notes')
p.add_argument('filename', help='path to a text file in kindle format')
args = p.parse_args()

# print welcome message

print("Kindle Scraper 1.0. Copyright 2011 Shubhro Saha")


try:
    f = open(args.filename, 'r')
except:
    print(("Failed to open the file %s." % args.filename))
    exit()

# split file into list of clippings' content and show how many found

clippingListChunks = f.read().split("==========")

print(str(len(clippingListChunks)) + " clippings found.")

# convert clipping chunks of content into list of Clipping objects

clippingList = []

del clippingListChunks[0]
del clippingListChunks[-1]

for c in clippingListChunks:
    clippingList.append(Clipping(c))
    
# identify all unique titles and give option to print their note contents by key

uniqueTitles = []

for c in clippingList:
    if c.title not in uniqueTitles:
        uniqueTitles.append(c.title)

i = 0
print("Please indicate the title you wish to retrieve highlights for.")
for title in uniqueTitles:
    print("[" + str(i) + "] " + title)
    i = i + 1
    
titleIndex = int(input("Title Index #: "))
title = uniqueTitles[titleIndex]

# bring together all highlights for that title

output = ""

for c in clippingList:
    if (c.title == title):
        if (c.type == "Highlight"):
            #output = output + c.content + "\n\n"
            print(c.content + "\n")
            
            
## write output to file
#
#f = open("output.txt", "w")
#f.write(output)
#
#print "All highlights have been written to file."
