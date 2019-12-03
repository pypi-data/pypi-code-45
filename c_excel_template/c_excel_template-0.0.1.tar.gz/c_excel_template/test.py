from c_excel_template import Excel_Template




file_name="example.xls"
example_sheet="Sheet1"
print_data={"test":{'test2':"ddd", 'test1': "BBB","d1":[{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1}]}}
dt1=[]
for i in range(1,120):
    dt1.append({"orderno":f"A{i}","sales":f"B{i}"})
print_data["test"]["d1"]=dt1
test=Excel_Template(file_name,example_sheet)
test.get_template_filed_info()
print("开始输出")
test.print_excel_with_template(save_name="test3.xls",print_data=print_data)
