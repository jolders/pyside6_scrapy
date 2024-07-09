import scrapy
#from books_scraper.books_scraper.items import BooksScraperItem
from ..items import BooksScraperItem
from scrapy.loader import ItemLoader

class BooksscraperSpider(scrapy.Spider):
    name = "booksscraper"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]
    cols = ["title", "price"]
    #cols = ["Title", "Link", "Image", "Info"]
    # custom_settings = {"REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7"}

    def parse(self, response):
        ebooks = response.css('article.product_pod')

        for article in ebooks:
            #title = article.css("h3 > a::attr(title)").get()
            #price = article.css("p.price_color::text").get()
            #yield {'title': title, 'price': price}

            # Using Item class
            #ebook_item = BooksScraperItem()
            #ebook_item['title'] = article.css("h3 a").attrib['title']
            #ebook_item['price'] = article.css("p.price_color::text").get()
            #yield ebook_item

            #loader = ItemLoader(item=BooksScraperItem())
            #loader.add_value('title', article.css("h3 a").attrib['title'])
            #loader.add_value('price', article.css("p.price_color::text").get())
            #yield loader.load_item()

            loader = ItemLoader(item=BooksScraperItem(), selector=article)
            loader.add_css('title', "h3 a::attr(title)")
            loader.add_css('price', "p.price_color::text")
            yield loader.load_item()





