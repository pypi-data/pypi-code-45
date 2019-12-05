import os
import string
#选择文件基板

#把csv文件中的参数填充到基板,并写入到scrapy工程中
#不仅要改写文件内容，而且要改写文件的名字

class GenSpiderFile(object):
    def __init__(self,spider_params):
        self.spider_params = spider_params
    #根据csv_params的参数找到合适的模板文件
    def chose_template(self,spider_param):
        template_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"spider_template")
        template_file_name = "spider.py.tmpl"


        return os.path.join(template_base_path,template_file_name)




    def render_spiderfile(self):

        for kwargs in self.spider_params:
            path = self.chose_template(kwargs)
            # print(path)
            with open(path, 'rb') as fp:
                raw = fp.read().decode('utf8')
            # print(kwargs)
            fields_xpaths = []
            for key in list(kwargs.keys()):
                if "detailpage_fields" in key:
                    # print(key)
                    fields_xpaths.append((key.replace("detailpage_fields_",""),kwargs[key]))
                    del kwargs[key]
            kwargs["fields_xpaths"] = fields_xpaths
            # print(kwargs)
            content = string.Template(raw).substitute(kwargs)
            #这里指定spiders的目录的路径
            # render_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scrapys","scrapys","spiders")
            #打包的路径
            render_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "spiders", "spiders", "spiders")
            render_path = render_base_path +"/"+kwargs['spider_name'] + ".py"

            with open(render_path, 'wb') as fp:
                fp.write(content.encode('utf8'))




if __name__ == '__main__':
    # base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"spider_template")
    # file_path = os.path.join(base_path,"spider_get_same_post.py.tmpl")
    # print(file_path)
    result = string.Template("aaa${name}bbb")
    result = result.substitute(name="777")

    print("----",result)
