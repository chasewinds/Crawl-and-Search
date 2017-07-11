# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstparseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    discribe = scrapy.Field()
    inputs = scrapy.Field()
    output = scrapy.Field()
    ex_input = scrapy.Field()
    ex_output = scrapy.Field()
    #E3 = scrapy.Field()

'''    discribe = dict(discribe)
    discribes = discribe.keys()
    filename = 'first'
    with open(filename,'wb')as f:
        f.write(discribes)
        f.write(inputs)
        f.write(output)
        f.write(ex_input)
        f.write(ex_output)
        '''