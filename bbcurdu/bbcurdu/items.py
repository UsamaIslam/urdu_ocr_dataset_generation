# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Field


class GuardianItem(scrapy.Item):
    news_page_url = Field()

    title_headlines  = Field()

    content_news = Field()

