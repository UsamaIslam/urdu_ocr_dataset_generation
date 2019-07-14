import scrapy
import os

from scrapy.spiders import CrawlSpider
from bbcurdu.items import GuardianItem

print(os.getcwd())


class BBCSpider(CrawlSpider):
    name = "bbc"
    allowed_domains = ["bbc.com"]

    def urlFunc():
        groups_list = ['pakistan', 'regional', 'entertainment', 'sport', 'science', 'world', 'media/audio', 'media/photogalleries']
        url_list = ["https://www.bbc.com/urdu"]
        for group in groups_list:
            url = "https://www.bbc.com/urdu/" + group
            url_list.append(url)
        # print(url_list)
        return url_list

    start_urls = urlFunc()

    def parse(self, response):

        # for news title and main url
        for sel in response.xpath("//*[@class='faux-block-link__overlay-link']"):
            item = GuardianItem()

            news_url = sel.xpath("@href").extract_first()

            if news_url is not None:
                if news_url.startswith("http"):
                    item['news_page_url'] = news_url
                    request = scrapy.Request(item['news_page_url'], callback=self.parseSpecialNewsDetails)
                else:
                    item['news_page_url'] = "https://www.bbc.com" + news_url
                    request = scrapy.Request(item['news_page_url'], callback=self.parseNewsDetails)

                request.meta['item'] = item
                yield request


    def parseNewsDetails(self, response):
        item = response.meta['item']
        item = self.getNewsDetails(item, response)
        return item

    # Data source written to file from main news page
    def getNewsDetails(self, item, response):
        news_title = response.xpath("//*[@class='story-body__h1']/text()").extract_first().encode('utf-8')
        if news_title is not None:
            item['title_headlines'] = news_title
        else:
            item['title_headlines'] = "Not Found"

        lNewsContent = response.xpath("//*[@class='story-body__inner']/p/text()").extract()
        news_content = ('\n'.join(lNewsContent)).encode('utf-8')
        if news_content is not None:
            item['content_news'] = news_content
        else:
            item['content_news'] = "Not Found"

        with open('first_file.txt', 'a+') as fp:
            fp.write('{0}\n\n{1}\n\n\n\n'.format(item['title_headlines'], item['content_news']))

        with open('second_file.txt', 'a+') as fp1:
            fp1.write('{0}\n\n'.format(item['title_headlines']))

        return item


    def parseSpecialNewsDetails(self, response):
        for sel in response.xpath("//*[@class='faux-block-link__overlay-link']"):
            item = GuardianItem()

            news_url = sel.xpath("@href").extract_first()

            if news_url is not None:
                item['news_page_url'] = "https://www.bbc.com" + news_url
                request = scrapy.Request(item['news_page_url'], callback=self.parseNewsDetails)
                request.meta['item'] = item
                yield request
