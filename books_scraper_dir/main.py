import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot
from ui_mainwindow import Ui_MainWindow
# SCRAPY
from scrapy.crawler import CrawlerProcess
from books_scraper.books_scraper.spiders.booksscraper import BooksscraperSpider
from scrapy.settings import Settings
from books_scraper.books_scraper import settings as my_settings

#     pyside6-uic mainwindow.ui -o ui_mainwindow.py

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.scrapystart)
        self.ui.btn_exit.clicked.connect(self.close)

    @Slot(dict)
    def update_data(self, item):
        #print(item.values())
        title = item.get('title')
        price = item.get('price')

        #self.ui.textBrowser.insertPlainText("RUNNING in UPDATE_DATA")
        self.ui.textBrowser.insertPlainText(str(title) + "\n")
        self.ui.textBrowser.insertPlainText(str(price) + "\n")

    def scrapystart(self):
        print("I AM SCRAPY START")
        #settings = dict()
        #settings['USER_AGENT'] = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0'
        #settings['ITEM_PIPELINES'] = {'books_scraper.books_scraper.pipelines.BooksScraperPipeline': 1}
        #process = CrawlerProcess(settings=settings)

        crawler_settings = Settings()
        crawler_settings.setmodule(my_settings)
        process = CrawlerProcess(settings=crawler_settings)


        # Set a reference to the window in the spider
        BooksscraperSpider.window = window

        process.crawl(BooksscraperSpider)
        process.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
