import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://fr.wikipedia.org/wiki/Catégorie:Personnage_d%27animation']

    def parse(self, response):
        for title in response.css('div#mw-pages div.mw-category li'):
            yield {'character': title.css('a ::text').extract_first()}