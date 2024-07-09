# pip install openpyxl
from openpyxl import Workbook
import queue


class BooksScraperPipeline:
    def __init__(self):
        self.data_queue = queue.Queue()

    def open_spider(self, spider):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.title = "ebooks"

        self.sheet.append(spider.cols)


    def process_item(self, item, spider):

        #print("<<<<----RUNNING PIPELINES---->>>", item['title'])
        #print("<<<<----RUNNING PIPELINES---->>>", item['price'])
        #self.data_queue.put(item)
        dictitems = {'title': item['title'], 'price': item['price']}
        self.data_queue.put(dictitems)

        # Ebooks xlsx
        #self.sheet.append([item['Title'], item['Link'], item['Image'], item['Info']])
        self.sheet.append([item['title'], item['price']])

        return item  # So it prints to the terminal

    def close_spider(self, spider):
        from PySide6.QtCore import Signal, QObject

        class Communicate(QObject):
            data_signal = Signal(dict)

        self.comm = Communicate()
        self.comm.data_signal.connect(spider.window.update_data)

        while not self.data_queue.empty():
            item = self.data_queue.get()
            self.comm.data_signal.emit(item)

        self.workbook.save("ebooks.xlsx")
