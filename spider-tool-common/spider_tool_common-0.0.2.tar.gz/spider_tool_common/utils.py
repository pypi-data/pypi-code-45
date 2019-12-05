
import csv
import pymongo
import json
# 以双引号 括起来  csv文件要统一引号格式，统一用双引号括起来
def read_csvfile(csvfile):
    csv_list = []
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        for line in reader:
            csv_list.append(line)
    return csv_list


#db.createUser({user:'spider',pwd:'spider',roles:[{role:'readWrite',db:'scrapy_spider'}]})
class MongoExecute(object):
    def __init__(self):

        mongoclient = pymongo.MongoClient()
        self.spider_collection = mongoclient.scrapy_spiders_common["spider"]

    def insert(self,dic):
        self.spider_collection.insert(dic)
        print("插入成功")
    def delete(self,dic):
        self.spider_collection.remove(dic)
        print("删除成功")
    def update(self,dic,newdic):
        self.spider_collection.update(dic,newdic)
        print("更新成功")
    #db.spider.find({'spider_name':'spider1'}).sort({_id:-1}).limit(1)
    def find(self,dic):
        data = self.spider_collection.find(dic)
        return data

    def get_spidername(self):
        return self.spider_collection.distinct("spider_name")

if __name__ == '__main__':
    # csv_file = "/home/yhl/桌面/test.csv"
    # print(read_csvfile(csv_file))

    mongoexecute = MongoExecute()

    data_dict ={
        "spider_name": "zj_jdggzy_bidding",
        "loop_num": "10",
        "start_index": "1",
        "multi_factor":"25",
        "pagelist_get_index": "",
        "pagelist_groups_resolving": "//table[@class='GridView']//tr[@class='Row']",
        "pagelist_url_resolving": ".//a/@href",
        "detailpage_fields_prvnce_name": "浙江省",
        "detailpage_fields_latn_name": "杭州市",
        "detailpage_fields_country_name": "建德市",
        "detailpage_fields_inter_name": "杭州市公共资源交易中心建德分中心",
        "detailpage_fields_table_names": "dict_winbidder_test_01",
        "detailpage_fields_inter_type": "2",
    }

    # data_dict ={
    #     "spider_name": "zj_jdggzy_bidding",
    #     "tender_winbidder": "w",
    #     #这些参数是为了获得正确的模板
    #     "pagelist_request_type": "post",
    #     "pagelist_post_index_formdata": "1",
    #     "pagelist_request_get_is_same": "0",
    #     "detailpage_request_type": "get",  # 默认都是get
    #
    #     "loop_num": "10",
    #     "start_index": "1",
    #
    #     "pagelist_get_index": "",
    #     "pagelist_get_index_1_url": "",
    #     "pagelist_get_index_other_url": "",
    #
    #     "pagelist_post_baseurl": "http://www.jdggzy.com/ProArticle/ProArticleList.aspx?ViewID=318&AfficheType=104",
    #     "pagelist_formdata": "GridViewer1$ctl18$BtnGoto_Go;GridViewer1$ctl18$NumGoto_{}",
    #
    #     "pagelist_groups_resolving": "//table[@class='GridView']//tr[@class='Row']",
    #     "pagelist_title_resolving": ".//a/@title",
    #     "pagelist_date_resolving": ".//td[3]/text()",
    #     "pagelist_url_resolving": ".//a/@href",
    #
    #     "detailpage_fields_prvnce_name": "浙江省",
    #     "detailpage_fields_latn_name": "杭州市",
    #     "detailpage_fields_country_name": "建德市",
    #     "detailpage_fields_inter_name": "杭州市公共资源交易中心建德分中心",
    #     "detailpage_fields_table_names": "dict_	winbidder_test_01",
    #     "detailpage_fields_inter_type": "2",
    # }

    mongoexecute.insert(data_dict)

    # spider_names = mongoexecute.get_spidername()
    # for spider_name in spider_names:
    #     print(spider_name)
    #     aa = mongoexecute.find({"spider_name": spider_name}).sort([("_id",-1)]).limit(1)
    #
    #     for i in aa:
    #         print(i)
