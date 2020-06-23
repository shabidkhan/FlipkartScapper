# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlipkartItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    price = scrapy.Field()
    memory = scrapy.Field()
    screen = scrapy.Field()
    camera = scrapy.Field()
    battery = scrapy.Field()
    processor = scrapy.Field()
    warranty = scrapy.Field()
    
