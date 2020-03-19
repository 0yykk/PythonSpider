# -*- coding: utf-8 -*-
import pymysql
#import re
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangspiderPipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host="127.0.0.1",port=3306,user="root",passwd="#",db="dangdangspider")
        #pat="\d+\.?\d*"
        for i in range(0,len(item["title"])):
            title=item["title"][i]
            title=title.lstrip()
            link=item["link"][i]
            comment=item["comment"][i]
            price=item["price"][i]
        
            #print(title+":"+link+":"+comment)
            #print(itemprice)
            sql="insert into goods(title,link,comment,price)values('"+title+"','"+link+"','"+comment+"','"+str(price)+"')"
            #print(sql)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as err:
                print(err)
        conn.close()
        return item
