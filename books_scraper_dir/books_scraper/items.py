from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst

def get_price(txt):
    return float(txt.replace('£', ''))

class BooksScraperItem(Item):
    #print("BooksScraperItem-ItemITEMLOADER")
    title = Field(output_processor=TakeFirst())
    price = Field(input_processor=MapCompose(get_price), output_processor=TakeFirst())


