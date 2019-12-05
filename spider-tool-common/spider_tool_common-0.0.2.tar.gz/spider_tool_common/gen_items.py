import string
import os
class GenItem(object):
    def __init__(self,csv_params):
        self.csv_params = csv_params
        self.item_template_path = os.path.join(os.path.dirname(__file__),
                                               "item_template","item_template.py.tmpl")
    def gen_items(self):

        for i in self.csv_params:
            num = 1
            item_dict = {}
            for k,v in i.items():
                if 'detailpage_fields_' in k:
                    k = k.replace("detailpage_fields_","")

                    item_dict[str(num)] = k
                    with open(self.item_template_path,"rb") as fp:
                        raw = fp.read().decode('utf8')

                    content = string.Template(raw).substitute(item_dict)

                    render_base_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                    "scrapys", "scrapys",
                                                    "spiders")
                    # render_path = render_base_path + "/" + kwargs['spider_name'] + ".py"
                    #
                    # with open(render_path, 'wb') as fp:
                    #     fp.write(content.encode('utf8'))


