# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 22:56:25 2020

@author: Sakib
"""

import scrapy
from ..items import BbcScrapeDataEngineerItem

class BBC_spider(scrapy.Spider):
    name = 'BBC'
    page_number = 2
    story = None
    start_urls = ['https://www.bbc.co.uk/search?q=coronavirus']
     
    def parse(self, response):
        items = BbcScrapeDataEngineerItem()
        all_news_containers = response.css('.ett16tt11')

        for news in all_news_containers:
            try:
#                print(news)
                keywords = news.css('.ecn1o5v0 span::text').extract()

                if keywords[1] == 'News' or 'Programmes':
                    
                    #Date & Tag
                    items['Date'] = keywords[0]
                    items['Tag'] = keywords[2]
                    items['Type'] = keywords[1]
                    
                    #Headlines
                    headings = news.css('.ett16tt7 span::text').extract_first()
                    items['Headline'] = headings
#                    yield {'title': headings}
                    
                    #HyperLinks
                    link = news.css('.ett16tt4 a::attr(href)').get()
                    items['HyperLinks'] = link
                    if keywords[1] == 'News':
                        yield response.follow(link, callback = self.parse_article, meta=items)
                    else:
                        story = news.css('.ett16tt10 p::text').extract()
                        items['Text'] = story
                        yield items
                        
                        
            except IndexError: #omits first two or three classes as they are not relevent
                continue
            
        next_page =  'https://www.bbc.co.uk/search?q=corona&page=' + str(BBC_spider.page_number)
        if BBC_spider.page_number <=10:
            yield response.follow(next_page, callback = self.parse)
            BBC_spider.page_number +=1
            
    def parse_article(self, response):
        items = response.meta
#        items = BbcScrapeDataEngineerItem()
        story = response.css('.story-body__inner p::text').extract()
        
        if len(story) == 0:
            story = response.css('.vxp-media__summary p::text').extract()
        items['Text'] = story
        yield items

#        
