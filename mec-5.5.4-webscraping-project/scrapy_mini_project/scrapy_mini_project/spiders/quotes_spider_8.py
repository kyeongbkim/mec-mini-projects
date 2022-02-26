import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes-8"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        anchors = response.css('ul.pager a')
        yield from response.follow_all(anchors, callback=self.parse)
