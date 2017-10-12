# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector

def scrape_data(xpath_info):
    item = []
    for i in xpath_info:
        item.append(i)

    return item

class NewsSpider(scrapy.Spider):
    name = "live_hindustan"

    allowed_domains = ['livehindustan.com']

    start_urls = [
    'http://www.livehindustan.com/national/news-1',
    'http://www.livehindustan.com/international/news-1',
    'http://www.livehindustan.com/sports/news-1',
    'http://www.livehindustan.com/business/news-1',
    'http://www.livehindustan.com/cricket/news-1',
    'http://www.livehindustan.com/entertainment/news-1',
    'http://www.livehindustan.com/gadgets/news-1',
    'http://www.livehindustan.com/lifestyle/news-1'
    ]

    def parse(self, response):
        news_titles = scrape_data(Selector(response).xpath('//div[@class="upper-first "]/h4/a/text()').extract())

        news_urls = scrape_data(Selector(response).xpath('//div[@class="upper-first "]/h4/a/@href').extract())

        image_urls = scrape_data(Selector(response).xpath('//div[@class="upper-first "]/a/img/@src').extract())

        news_summary = scrape_data(Selector(response).xpath('//div[@class="upper-first "]/div/p/text()').extract())

        hindi_month = ['जनवरी,','फरवरी,','मार्च,','अप्रैल,','मई,','जून,','जुलाई,','अगस्त,','सितंबर,','अक्तूबर,','नवम्बर,','दिसम्बर,']
        english_month = ['JAN','FEB','MAR','APR','MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']

        news_date_time = scrape_data(Selector(response).xpath('//div[@class="list-time-tags tags-list"]/span/text()[not(ancestor::*[@class="list-tags"])]').extract())
        date_time_list = []
        for i in news_date_time:
            if i != ' ':
                for hm,em in zip(hindi_month,english_month):
                    i = i.replace(hm.decode('UTF-8'),em)

                date_time_list.append(i)

        for i,j,k,l,m in zip(news_titles,news_urls,image_urls,news_summary,date_time_list):
            print "News title : " + i
            print "News link : " + 'http://www.livehindustan.com' + j
            print "News image url : " + k
            print "News summary : " + l
            print "News date & time : " + m
            print "\n"

        next_page = 'http://www.livehindustan.com' + response.xpath('//ul[@class="pagination"]/li/a/@href').extract()[-1]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
