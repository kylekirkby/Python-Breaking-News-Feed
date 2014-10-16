import xml.etree.ElementTree as etree
import urllib.request


feed = urllib.request.urlopen("http://feeds.bbci.co.uk/news/world/rss.xml")
feedData = feed.read()

with open("feedNe2w.xml",mode="w") as feedFile:
    for line in feedData.decode("utf-8"):
        feedFile.write(line)

#tree = etree.parse("feedNew.xml")
root = etree.fromstring(feedData.decode("utf-8"))

item = root.findall('channel/item')

newsFeed = []

for entry in item:
    newEntry = []
    #get description, url, and thumbnail
    title = entry.findtext('title')
    link = entry.findtext('link')
    desc = entry.findtext('description')
    thumb = entry.findtext('media:thumbnil url')
    published  = entry.findtext('pubDate')
    
    newEntry.append(title)
    newEntry.append(link)
    newEntry.append(desc)
    newEntry.append(thumb)
    newEntry.append(published)

    newsFeed.append(newEntry)

for i in range(0,len(newsFeed)):
    print("{0}. {1}".format(i + 1,newsFeed[i][0]))
