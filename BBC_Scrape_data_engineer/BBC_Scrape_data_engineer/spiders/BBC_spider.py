# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:56:25 2020

@author: Sakib
"""

import scrapy
from ..items import BbcScrapeDataEngineerItem

class BBC_spider(scrapy.Spider):
    name = 'BBC'
    start_urls = ['https://www.bbc.com/']
     
    def parse(self, response):
        items = BbcScrapeDataEngineerItem() #Temporary container
        all_news_containers = response.css('.media__content')
        
        for news in all_news_containers:
#            print(news)
            try:
                #Headlines
                headings = news.css('.media__link::text').extract_first()
                headings = headings.strip()
#                yield {'titletext':headings}
                items['Headline'] = headings
                
                #HyperLinks
                link = news.css('a').xpath("@href").extract_first()
                link = link.strip()
#                yield {'titletext':headings}
                items['HyperLinks'] = link
#                print(link)
                
                #TAG
                tag = news.css('.tag::text').extract_first()
                tag = tag.strip()
#                yield {'titletext':headings}
                items['Tag'] = tag
                
                
                yield items
            except AttributeError: #eleminating the Nonetype attribute
                continue
        
