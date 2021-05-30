import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    custom_settings = {
        'FEED_URI': 'veriler2.csv',
        'FEED_FORMAT': 'csv'
                      }

    def start_requests(self):
        url = 'https://www.trendyol.com/televizyon-x-c104156'
        yield scrapy.Request(url)

    def parse(self, response):
        marka = response.xpath('.//span[@class="prdct-desc-cntnr-name hasRatings"]/text()').extract()
        yield {'brand': marka}
