#需要生成爬虫的启动文件
import os
import string
class GenStartSpier(object):
    def __init__(self,spider_params):
        self.spider_params = spider_params

    def chose_template(self):
        template_base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "main_template")
        template_file_name = "spider_tool_common.py.tmpl"

        return os.path.join(template_base_path, template_file_name)
    def handleresult(self):
        for kwargs in self.spider_params:
            path = self.chose_template()
            with open(path, 'rb') as fp:
                raw = fp.read().decode('utf8')
            # print(kwargs)
            field_names = []
            for key in list(kwargs.keys()):
                if "detailpage_fields" in key:
                    # print(key)
                    field_names.append(key.replace("detailpage_fields_",""))
            kwargs["field_names"] = ",".join(field_names)
            content = string.Template(raw).substitute(kwargs)
            #这里指定spiders的目录的路径
            # render_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "scrapys","scrapys")
            #
            render_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "spiders", "spiders")

            render_path = render_base_path +"/spider_tool_common.py"
            #
            with open(render_path, 'wb') as fp:
                fp.write(content.encode('utf8'))

