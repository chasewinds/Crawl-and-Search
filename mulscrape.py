import scrapy
from firstparse.items import FirstparseItem
#from scrapy.spiders import Rule
#from scrapy.linkextractors import LinkExtractor

class MultiSpider(scrapy.Spider):
    name = 'mulscrape'
    allowed_domains = ['bailian.openjudge.cn']
    start_urls = ['http://bailian.openjudge.cn/practice/']

    def start_requests(self):
        title_page_url = 'http://bailian.openjudge.cn/practice/'
        for i in range(3):
            topic_id = 1000 + i
            topic_url = title_page_url + str(topic_id) + '/'
            yield scrapy.Request(topic_url,callback = self.parse_topic)

    def parse_topic(self,response):
        sel = scrapy.Selector(response)
        #print (response)
        
        item = FirstparseItem()
        item['discribe'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[1]/p').extract()[0]
        item['inputs'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[2]').extract()[0]
        item['output'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[3]').extract()[0]
        yield item
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''    
    def parse(self,response):
#        filename = response.url.split('/')[-2]#why [2]?
        print ('special parse...')
        print (response)
        for sel in response.xpath('/html'):
            print ('parse2...')
            item = FirstparseItem()
            item['discribe'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[1]').extract()
            item['inputs'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[2]').extract()
            item['output'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[3]').extract()
            item['ex_input'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[4]/pre').extract()
            item['ex_output'] = sel.xpath('//*[@id="pagebody"]/div/div[3]/dl[2]/dd[5]/pre').extract()
            print ('parse3...')
            yield item
'''


