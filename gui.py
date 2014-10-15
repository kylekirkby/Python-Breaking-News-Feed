from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys


class MainWindow(QMainWindow):

    """This is the main window for the breaking news feed application"""

    def __init__(self):

        super().__init__()

        self.icon = QIcon(QPixmap("./globe.png"))
        self.setWindowIcon(self.icon)
        
        self.setWindowTitle("Python Breaking News Feed")
        self.resize(500,300)

        self.initial_layout()

    def initial_layout(self):

        #widgets
        self.allNewsPushButton = QPushButton("All News")
        self.skyNewsPushButton = QPushButton("Sky News")
        self.bbcNewsPushButton = QPushButton("BBC News")
        self.yahooNewsPushButton = QPushButton("Yahoo News")

        #news feed button layout
        
        self.newsFeedButtonLayout = QHBoxLayout()
        self.newsFeedButtonLayout.addWidget(self.allNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.skyNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.bbcNewsPushButton)
        self.newsFeedButtonLayout.addWidget(self.yahooNewsPushButton)

        #allNews list view

        self.allNewsListView = QListView()

        #allNews widget
        
        
        #news feed button widget
        self.newsFeedButtonWidget = QWidget()
        self.newsFeedButtonWidget.setLayout(self.newsFeedButtonLayout)
        
        #mainLayout
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.newsFeedButtonWidget)
        self.mainLayout.addWidget(self.allNewsListView)

        #mainWidget
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)
        
        self.setCentralWidget(self.mainWidget)
if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    app.exec_()
