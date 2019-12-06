#!/usr/bin/python
# -*- coding: UTF-8 -*-
#载入必要的模块

from faker import Factory
from faker import Faker
from faker.providers import BaseProvider
import xlwt
import xlrd
import string


#letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","AA","BB","CC","DD"]
letter_list = ["A","B"]

class MyProvider(BaseProvider):

    def foo(self):

        return u'本地用户'

    def pwd(self):

        return '111'

class office:

    def write_excel(self,list):
        f = xlwt.Workbook()
        o = office()
        faker = Faker("zh_CN")
        faker.add_provider(MyProvider)
        sheet1 = f.add_sheet(u"样本%s" % list,cell_overwrite_ok=True)

        row0 = [u"用户名",u"姓名",u"组织",u"类型",u"密码"]
        #写第一行
        for i in range(0,len(row0)):
            #sheet1.write(0,i,row0[i],o.set_style('Calibri',220,True))
            sheet1.write(0,i,row0[i])

        #设置第一列列宽
        first_col=sheet1.col(0)
        first_col.width = 500*6 #8个英文字符
        '''colum0 = [faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                  ,faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name(),faker.user_name()\
                 ]
        '''         
        #写第一列
        #for i in range(0,len(colum0)):
        for i in range(0,10000):
            #sheet1.write(i+1,0,colum0[i],o.set_style('Calibri',220,False))
            #sheet1.write(i+1,0,colum0[i])
            #letter_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            #sheet1.write(i+1,0,faker.user_name()+str(i)+"A")
            sheet1.write(i+1,0,faker.user_name()+str(i)+list)

         #设置第二列列宽
        first_col=sheet1.col(1)
        first_col.width = 500*8
        '''colum1 = [faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                  ,faker.name(),faker.name(),faker.name(),faker.name(),faker.name()\
                 ]
        '''         
        #写第二列
        #for i in range(0,len(colum1)):
         #   sheet1.write(i+1,1,colum1[i])
        for i in range(0,10000):
            sheet1.write(i+1,1,faker.name())

        #设置第三列列宽
        first_col=sheet1.col(2)
        first_col.width = 500*12
        
        my_word_list = [u"研发部门",u"测试部门",u"研发部门\研发一部\海外支撑部",u"研发部门\研发一部",u"研发部门\研发二部",u"测试部门\测试一部",u"测试部门\测试二部",u"行政部门",u"行政部\前台",u"财务部",u"财务部\财务一部",u"财务部\财务总监部",u"人力资源部",u"人力资源部\福利部",u"人力资源部\福利部\海外部"]
        '''colum2 = [faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                  ,faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list),faker.random_element(my_word_list)\
                 ]
        '''
        
        #写第三列
        #for i in range(0,len(colum2)):
         #   sheet1.write(i+1,2,u"全网用户\总公司\\"+colum2[i])
            
        
        for i in range(0,10000):      
            sheet1.write(i+1,2,u"全网用户\总公司\\"+list+u"阿里\\"+faker.random_element(my_word_list))

        #设置第四列列宽
        first_col=sheet1.col(3)
        first_col.width = 500*11
        '''colum3 = [faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ,faker.foo(),faker.foo(),faker.foo(),faker.foo(),faker.foo()\
                  ]
        '''          
        #写第四列
        #for i in range(0,len(colum3)):
         #   sheet1.write(i+1,3,colum3[i])
            
        for i in range(0,10000):
            sheet1.write(i+1,3,faker.foo())

        #设置第五列列宽
        first_col=sheet1.col(4)
        first_col.width = 500*9
        '''colum4 = [faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                  ,faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd(),faker.pwd()\
                 ]

        '''
        
        #写第五列
        #for i in range(0,len(colum4)):
         #   sheet1.write(i+1,4,colum4[i])

        for i in range(0,10000):
            sheet1.write(i+1,4,faker.pwd())

        f.save("Result\\user_"+list+".xls")

        return True

#end--------------------------------------------------------
if __name__ == "__main__":
    app = office()
    
    for i in letter_list:
        app.write_excel(i)