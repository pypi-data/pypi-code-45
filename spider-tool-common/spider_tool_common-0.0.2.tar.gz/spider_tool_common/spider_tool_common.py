from spider_tool_common.utils import MongoExecute
from spider_tool_common.gen_spider import GenSpiderFile
from spider_tool_common.gen_main import GenStartSpier
import os
def execute(mongoexecute):
    spider_names = mongoexecute.get_spidername()
    spider_params = []
    for spider_name in spider_names:
        spider_cursor = mongoexecute\
            .find({"spider_name": spider_name})\
            .sort([("_id", -1)]).limit(1)
        for spider_param in spider_cursor:
            spider_params.append(spider_param)
            # 获得爬虫的参数 并据此找到模板 插入参数 生成代码 (只针对spider文件)
    #生成爬虫代码
    GenSpiderFile(spider_params).render_spiderfile()
    #启动爬虫程序并把结果导入到mongodb，接着把mongodb的结果导出到csv文件
    GenStartSpier(spider_params).handleresult()




def insert_params(spider_params):
    mongoexecute = MongoExecute()
    mongoexecute.insert(spider_params)


    data_dict = {
        "spider_name": "zj_jdggzy_bidding",
        "loop_num": "10",
        "start_index": "1",
        "multi_factor": "25",
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
    # mongoexecute.insert(data_dict)

def crawl_data():
    mongoexecute = MongoExecute()
    execute(mongoexecute)

    #需要找到提前指定好的spider程序的路径，找到启动爬虫的main.py方法，然后启动执行
    #执行是否成功没有验证
    spider_path = "/spiders/spiders/spider_tool_common.py"
    os.popen("python3 "+spider_path)

if __name__ == '__main__':
    mongoexecute = MongoExecute()
    execute(mongoexecute)























    # if isdeploy == "nodp":
    #     pass
    #     #正常处理数据，在试着爬取 以及那入库 这块都
    #
    #     #读取mongodb,读取配置
    #     #先获得爬虫的名字 ，每次获得爬虫的最新的配置
    #
    #
    #
    #
    #     #每次读取都会重新生成新的爬虫代码并覆盖原来的爬虫代码
    #
    #     #配置文件的参数展示
    #
    #     #是否是test模式  从命令行得到
    #     #要打印日志
    #     #csv文件包括三个部分
    #     #一是具体的爬虫配置选项(包括字段选项)
    #     #二是爬虫的反爬措施
    #     #三是爬虫的运行参数
    #
    #     # start_crawl()
    #
    #
    #     # if isinputdb == "db":
    #     #     #进入数据库，执行pipeline操作
    #     #     pass
    #
    # else:
    #     pass
    #
    #     # #执行部署的操作  指定工程名 项目名
    #     # if isinputdb == "nodb":
    #     #     raise Exception("没有指定数据库")
    #
    #
    #
    #
    #
    # #如果是没有创建项目就创建 默认一开始就创建好默认项目
    # #新的spider文件生成
    # #如果创建了项目看是有字段的修改 ，根据是否修改字段看是否需要重新生成新的字段模板
    # #是否有新的配置，根据是否有新的配置看是否会生成新的配置文件


