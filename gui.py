from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

from NewsFeedRSS import *


class MainWindow(QMainWindow):

    """This is the main window for the breaking news feed application"""

    def __init__(self):

        super().__init__()

        self.icon = QIcon(QPixmap("./globe.png"))
        self.setWindowIcon(self.icon)
        
        self.setWindowTitle("Python Breaking News Feed")
        self.resize(500,300)

        #news

        self.allNews = None
        self.bbcNews = None
        self.skyNews = None
        self.yahooNews = None
        self.rtNews = None

        self.initial_layout()
    def getAllNews(self):
        feed = NewsFeedRSS()
        feed.getRssFeedData

        self.newsListView.clear()

        #all news
        allNews = []

        #get bbc news

        bbcResults = feed.getRssFeedData(feed.bbcNewsLink)
        skyResults = feed.getRssFeedData(feed.skyNewsLink)
        yahooResults = feed.getRssFeedData(feed.yahooNewsLink)

        for each in bbcResults:
            old = each[0]
            each[0] = "BBC - " + old
            allNews.append(each)
        for each in skyResults:
            old = each[0]
            each[0] = "SKY - " + old
            allNews.append(each)
        for each in yahooResults:
            old = each[0]
            each[0] = "YHO - " + old
            allNews.append(each)


        allNewsResults = sorted(allNews)

        for each in allNews:
            self.newsListView.addItem(each[0])

        self.allNews = allNewsResults
        
    def getBbcNews(self):
        #get the bbc news results
        feed = NewsFeedRSS()
        results = feed.getRssFeedData(feed.bbcNewsLink)
        #clear the news list view widget
        self.newsListView.clear()
        for news in results:
            
            self.newsListView.addItem(news[0])

        self.bbcNews = results

    def getSkyNews(self):
        
        feed = NewsFeedRSS()
        results = feed.getRssFeedData(feed.skyNewsLink)
        #clear the news list view widget
        self.newsListView.clear()
        for news in results:
            
            self.newsListView.addItem(news[0])

        self.skyNews = results
                    
    def getYahooNews(self):
        feed = NewsFeedRSS()
        results = feed.getRssFeedData(feed.yahooNewsLink)
        #clear the news list view widget
        self.newsListView.clear()
        for news in results:
            self.newsListView.addItem(news[0])


        self.yahooNews = results
    def getRtNews(self):
        feed = NewsFeedRSS()
        results = feed.getRTNewsFeed()
        #clear the news list view widget
        self.newsListView.clear()
        for news in results:
            self.newsListView.addItem(news[0])


        self.rtNews = results

    def searchResults(self):
        currentItems = []
        query = self.searchField.text()
        if query != "":
            self.newsListView.clear()
            for each in self.allNews:
                if query.lower() in each[0].lower():
                    self.newsListView.addItem(each[0])
                elif query in each[1]:
                    self.newsListView.addItem(each[0])
                elif query in each[2]:
                    self.newsListView.addItem(each[0])
    def viewNewsArticleLayout(self):
        self.backButon = QPushButton("Back")

        self.title = QLabel("News Title")
        self.description = ""
            
    def initial_layout(self):

        #widgets
        self.allNewsPushButton = QPushButton("All News")
        self.skyNewsPushButton = QPushButton("Sky News")
        self.bbcNewsPushButton = QPushButton("BBC News")
        self.rtNewsPushButton = QPushButton("RT News")
        self.yahooNewsPushButton = QPushButton("Yahoo News")

        self.searchField = QLineEdit()

        #news feed button layout
        
        self.newsFeedButtonLayout = QHBoxLayout()
        self.newsFeedButtonLayout.addWidget(self.allNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.skyNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.bbcNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.yahooNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.rtNewsPushButton)

        #allNews list view

        self.newsListView = QListWidget()

        #allNews widget
        
        
        #news feed button widget
        self.newsFeedButtonWidget = QWidget()
        self.newsFeedButtonWidget.setLayout(self.newsFeedButtonLayout)
        
        #mainLayout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.newsFeedButtonWidget)
        self.mainLayout.addWidget(self.newsListView)
        self.mainLayout.addWidget(self.searchField)

        #mainWidget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        
        self.setCentralWidget(self.mainWidget)

        #set button connections

        self.allNewsPushButton.clicked.connect(self.getAllNews)
        self.skyNewsPushButton.clicked.connect(self.getSkyNews)
        self.bbcNewsPushButton.clicked.connect(self.getBbcNews)
        self.rtNewsPushButton.clicked.connect(self.getRtNews)
        self.yahooNewsPushButton.clicked.connect(self.getYahooNews)

        self.searchField.textChanged.connect(self.searchResults)
        
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
