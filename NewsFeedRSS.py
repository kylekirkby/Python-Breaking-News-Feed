
import xml.etree.ElementTree as etree
import urllib.request


class NewsFeedRSS():
    """This class collects data from various news feeds"""

    def __init__(self):

        self.bbcNewsLink = "http://feeds.bbci.co.uk/news/world/rss.xml"
        self.skyNewsLink = "http://feeds.skynews.com/feeds/rss/world.xml"
        self.yahooNewsLink = "http://news.yahoo.com/rss/world"

    def getRssFeedData(self,rssLink):
        
        feed = urllib.request.urlopen(rssLink)
        feedData = feed.read()

        if rssLink == self.bbcNewsLink:
            fileName = "bbcNews.xml"
        elif rssLink == self.skyNewsLink:
            fileName = "skyNews.xml"
        elif rssLink == self.yahooNewsLink:
            fileName = "yahooNews.xml"

        
        with open(fileName,mode="w") as feedFile:
            for line in feedData.decode("utf-8"):
                feedFile.write(line)

        #tree = etree.parse(fileName)
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

        return newsFeed
