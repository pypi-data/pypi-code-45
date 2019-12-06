#!/usr/bin/python
# -*- coding: UTF-8 -*-
from jpype import *
from faker import Factory
from faker import Faker
import os.path
import random
import pycurl
from StringIO import StringIO
import xlrd
import base64
import multiprocessing
import threading

boolean_list = ["TRUE","FALSE"]
tables = ["the_first_table","the_second_table","my_third_table","my_forth_table","my_fifth_table","my_sixth_table","my_seventh_table"]
keyword1 = ["十六开本","大众市场纸皮书版式","启蒙读物","文摘通报","学位论文","组稿编辑","胶粘装订联动线","青少年读物","文稿代理人","出版日期和书价"]
keyword2 = ["会议建议","会议指出","持续进行","会议充分肯定了","正式启动","会议安排","会议倡议","会议要求贯彻落实","各部门依照","整个会议共持续"]
keyword3 = ["政治主张","自治请愿","支持新疆独立","恐怖组织","勾结外国","打倒资本主义","基督教民主主义","权威主义","公共言论的抑制","言论自由受到"]



def CreateDataBase(database):
   str = "create database %s;" % database
   return str

def UseDataBase(database):
   str = "use %s;" % database
   return str

def CreateTable(table):
   str = "CREATE TABLE %s (\
   id BIGINT,\
   flag BOOLEAN,\
   number FLOAT,\
   dnumber DOUBLE,\
   name  STRING,\
   word1  STRING,\
   word2  STRING,\
   word3  STRING,\
   PRIMARY KEY(id)\
   )\
   partition by hash partitions 8\
   STORED AS KUDU\
   TBLPROPERTIES('kudu.master_addresses' = '127.0.0.1','kudu.num_tablet_replicas' = '1');" % table
   return str

def getStr(table,id,flag,num,dnum,ip,key1,key2,key3):
   str = "insert into %s values(%s,%s,%s,%s,'%s','%s','%s','%s');" % (table,id,flag,num,dnum,ip,key1,key2,key3)
   return str

def run():
   faker = Faker("zh_CN")
   database = "test2"
   table = "my_seventh_table"
   f = open('Result\\sql','a')
   f.writelines(CreateDataBase(database) + "\n")
   f.writelines(UseDataBase(database) + "\n")
   for table in tables:
      f.writelines(CreateTable(table) + "\n")
      for i in xrange(1,101):
         f.writelines(getStr(table,i,faker.random_element(boolean_list),random.uniform(1,10000),\
            random.uniform(1,10000),faker.ipv4(),faker.random_element(keyword1),\
            faker.random_element(keyword2),faker.random_element(keyword3)) + "\n")
   f.close()
if __name__ == "__main__":
   run()
