# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BbcScrapeDataEngineerItem(scrapy.Item):
    #Extracted Data -> Temporary Container
    # define the fields for your item here like:
    # name = scrapy.Field()
    Date = scrapy.Field()
    Headline = scrapy.Field()
    Type = scrapy.Field()
    HyperLinks = scrapy.Field()
    Tag = scrapy.Field()
    Text = scrapy.Field()
    