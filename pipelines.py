# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import re
import pymysql.cursors
from scrapy.exceptions import DropItem
#from firstparse.items import FirstparseItem

#os.makedirs(r'e:/scrapys/dict/')
os.chdir('e:/scrapys/dict')
topic_num = 1000
print('outside pipeline function')
class FirstparsePipeline(object):
    def process_item(self,item,spider):
        global topic_num
        filename = str(1000 + topic_num)
        names = filename + '.txt'
        with open(names,'w') as fp:
            for key,value in item.items():
                print (type(key))
                print (type(value))
                fp.write("{}:{}".format(key,value))
            fp.write('\n')
        print ('Inside process_item function')

        #print(key,value)
        #print (item)

        topic_num += 1
    """
    def process_item(self, item, spider):
        print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
        key1 = item['discribe']
        key2 = item['inputs']
        key3 = item['output']
        print(type(item['inputs']))
        #Drop the topics include chinese
        #This step just store the english topics
        '''
        if item.get('discribe'):
            print(type(item['discribe']))
            item['discribe'] = item['discribe'].encode('utf-8')
            iters = str(item['discribe'])
            drop = re.search(r'[^\x00-\xff]',iters)
            if drop == None:
                print('waiting do not drop.......................................................')
            else:
                print('readly to drop ...........................................................')
                raise DropItem("this item content chinese %s" % item)

            '''
         #start connecte to database:
        global topic_num
        config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'zxcvbnm88',
            'database': 'first',
            'port': 3306,
            'use_unicode':True
        }
        connection = pymysql.connect(**config)
        #connection.set_character_set('utf8')
        print('already connected !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        topic_num += 1
        try:
            with connection.cursor() as cursor:
                '''
                i = 1
                if i == 1:
                    sql = 'insert into topics (topic_id,discribe,input,output) values (%s,%s,%s,%s)'
                    cursor.execute(sql,('h','f','fee','efe'));
                    discirbe = b'<p>Calculate a + b<p>'
                    inputs = '<dd>Two integer a,,b (0 < a,b < 10)</dd>'
                    output = '<dd>Output a + b</dd>'
                    cursor.execute(sql,('47578',discirbe,inputs,output))
                '''
                sql = 'insert into topics (topic_id,discribe,input,output) values (%s,%s,%s,%s)'
                if item.get('discribe'):
                    #for i in range(len(item['discribe'])):
                    topic_serial = str(topic_num)
                    print('...................................................')
                    print (type(key1))
                    print(type(key2))
                    print(type(key3))
                    try:
                        cursor.execute(sql,(topic_serial,key1,key2,key3));
                    except:
                        print('in except >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
                        raise DropItem ("this item content chinese %s" % item)

            print('befor commit%%%%%%%%%%%%%%%%%%%%%%')
            connection.commit()
        finally:
            connection.close()
        return item
"""
