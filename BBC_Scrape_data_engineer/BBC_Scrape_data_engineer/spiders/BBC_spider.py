# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:56:25 2020

@author: Sakib
"""

import scrapy
from ..items import BbcScrapeDataEngineerItem

class BBC_spider(scrapy.Spider):
    name = 'BBC'
    start_urls = ['https://www.bbc.co.uk/search?q=corona']
     
    def parse(self, response):
        items = BbcScrapeDataEngineerItem() #Temporary container
        all_news_containers = response.css('.ett16tt11')

        for news in all_news_containers:
            try:
                print(news)
                keywords = news.css('.ecn1o5v0 span::text').extract()

                if keywords[1] == 'Programmes':
                    
                    #Date & Tag
                    items['Date'] = keywords[0]
                    items['Tag'] = keywords[2]
                    yield {'title': keywords[0]}
                    yield {'title': keywords[2]}
                    
                    #Headlines
                    headings = news.css('.ett16tt7 span::text').extract_first()
                    items['Headline'] = headings
                    yield {'title': headings}
                    
                    #HyperLinks
                    link = news.css('.ett16tt4 a::attr(href)').get()
                    items['HyperLinks'] = link
                    yield {'title': link}
                    
            except IndexError: #omits first two or three classes as they are not relevent
                continue
        
