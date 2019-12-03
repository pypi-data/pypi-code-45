from xlrd import open_workbook
import xlwt
from xlutils.copy import copy
from io import BytesIO
import re
import time


class Excel_Template(object):
    #template_file-模板文件,template_sheet-模板sheet,del_template-是否需要
    def __init__(self,template_file,template_sheet,del_template=True):
        self.template_file=template_file
        self.template_sheet=template_sheet
        self.del_template=del_template
    
    def end_process(self):
        # 处理插入图片等操作
        pass

    def flush_workboot_sheet(self):
        self.wb=copy(self.template_rb)
        self.ws=self.wb.get_sheet(self.wb.sheet_index(self.template_sheet))
        self.sheet_count=0
        
    def wb_save(self):
        file_name=f"""{self.save_name[0:len(self.save_name)-4]}{"" if self.wb_count==0 else f"_{self.wb_count}"}.xls"""
        if self.del_template:
            self.wb._Workbook__worksheets = [ worksheet for worksheet in self.wb._Workbook__worksheets if worksheet.name != self.template_sheet ]
        if bool(self.wb._Workbook__worksheets):
            self.end_process()
            self.wb.save(file_name)
            self.wb_count+=1        

    def copy_sheet(self,sheet_name):
        #因为如果wb太大影响运行效率，可以在这里调整多少个
        if len(self.wb._Workbook__worksheets)>101:
            self.wb_save()
            self.flush_workboot_sheet()
        sheet=self.wb.add_sheet(sheet_name,cell_overwrite_ok=True)
        for data in self.ws.merged_ranges:
            sheet.merged_ranges.append(data)
        for data in self.ws.cols:
            sheet.cols[data]=self.ws.cols[data]
        for data in self.ws.rows:
            sheet.rows[data]=self.ws.rows[data]
            sheet.rows[data]._Row__parent=sheet
        #将wb保存到文件流再打开，
        """
        如果不保存到文件流，所有Sheet都会变化。
        目前没有找到复制后,sheet可以唯一写入的方法。之后会做更新
        """
        fsio=BytesIO()
        self.wb.save(fsio)
        rb =open_workbook(file_contents=fsio.getvalue(),on_demand=True,formatting_info=True)
        self.wb=copy(rb)
        del fsio,rb
        self.ws=self.wb.get_sheet(self.wb.sheet_index(sheet_name))
        self.sheet_count+=1
        self.cur_row=0 
        end=time.time()

    def get_style(self,row,col):
        style=xlwt.XFStyle()        
        style_id=self.template_ws.row(row)._Row__cells[col].xf_idx
        style_list=self.template_wb._Workbook__styles._xf_x2id[style_id]
        # style_list[0]
        style.font=self.template_wb._Workbook__styles._font_x2id[0]
        for style_value in style_list:
            if type(style_value) ==xlwt.Formatting.Alignment:
                style.alignment=style_value
            if type(style_value) ==xlwt.Formatting.Borders:
                style.borders=style_value
            if type(style_value)==xlwt.Formatting.Pattern:
                style.pattern=style_value
            if type(style_value) == xlwt.Formatting.Protection:
                style.protection=style_value
        return style

    def sheet_write(self,pos_row,pos_col,value,with_style=True):

        if with_style:
            style=self.get_style(pos_row,pos_col)
            self.ws.write(pos_row,pos_col,value,style)
        else:
            self.ws.write(pos_row,pos_col,value)
        end=time.time()

    def get_template_filed_info(self):
        self.template_rb = open_workbook(filename=self.template_file,on_demand=True,formatting_info=True)
        self.template_rs = self.template_rb.sheet_by_name(self.template_sheet)
        self.template_wb=copy(self.template_rb)
        self.template_ws=self.template_wb.get_sheet(self.template_wb.sheet_index(self.template_sheet))
        field_dict={}
        # 获取配置信息
        for row in range(0,self.template_rs.nrows):
            for col in range(0,self.template_rs.ncols):
                value=str(self.template_rs.row_values(row)[col])
                #参数以 $变量$ 设置
                if bool(re.search("\$(\S+)\$",value)):
                    field_name=value[1:len(value)-1]
                    #明细表以 $明细表1.变量$ 设置
                    if re.search("\.",field_name):
                        main_field=field_name.split(".",1)[0]
                        detail_field=field_name.split(".",1)[1]
                        if main_field in field_dict:
                            #如果是开始结束标记
                            if detail_field =="start_id":
                                field_dict[main_field]["row_start"]=(row,col)
                            elif detail_field =="end_id":
                                field_dict[main_field]["row_end"]=(row,col)
                            else:
                                # 标记首条记录的开始行和结束行
                                if "min_row" not in field_dict[main_field] or field_dict[main_field]["min_row"]>row:
                                    field_dict[main_field]["min_row"]=row
                                if "max_row" not in field_dict[main_field] or  field_dict[main_field]["max_row"]<row:
                                    field_dict[main_field]["max_row"]=row
                                #明细行的坐标
                                if detail_field in field_dict[main_field]:
                                    field_dict[main_field][detail_field].append((row,col))
                                else:
                                    detail_dict[detail_field]=[(row,col)]
                        else:
                            #字典中不存在main_field
                            detail_dict={}
                            if detail_field =="start_id":
                                detail_dict["row_start"]=row
                            elif detail_field =="end_id":
                                detail_dict["row_end"]=row
                            else:
                                detail_dict["min_row"]=row
                                detail_dict["max_row"]=row
                                detail_dict[detail_field]=[(row,col)]
                        field_dict[main_field]=detail_dict
                    #主表字段
                    else:
                        if field_name in field_dict:
                            field_dict[field_name].append((row,col))
                        else:
                            field_dict[field_name]=[(row,col)]
        self.field_dict=field_dict

    def get_template_detail_info(self,filed):
        detail_field_dict=self.field_dict[filed]
        self.detail_field_dict=detail_field_dict
        self.row_start= detail_field_dict["min_row"] if "row_start" not in detail_field_dict else detail_field_dict["row_start"][0]
        self.row_end=len(sheet_data[filed])+self.row_start if "row_end" not in detail_field_dict else detail_field_dict["row_end"][0]
        self.row_min=detail_field_dict["min_row"]    
        self.row_max=detail_field_dict["max_row"]
        self.row_row=detail_field_dict["min_row"]-detail_field_dict["max_row"]+1
        self.row_range=int((self.row_end+1-self.row_start)/self.row_row) 


    def print_excel_with_template(self,save_name,print_data):
        self.get_template_filed_info()
        self.save_name=save_name
        self.wb_count=0
        #创建一个workbook
        self.flush_workboot_sheet()
        #Sheet_name
        for sheet_name in print_data:
            sheet_data=print_data[sheet_name]
            with_detail=False
            # 1-带明细数据输出
            for filed in sheet_data:
                if filed in self.field_dict:
                    if type(self.field_dict[filed]) == dict:
                        with_detail=True
                        #明细数据配置读取
                        self.get_template_detail_info(filed) 
                        #开始读取明细数据
                        self.cur_row=0    
                        self.page=0
                        for row_dict in sheet_data[filed]:
                            # 新一页输出，row_range：每页行数
                            if self.cur_row%self.row_range==0:
                                if self.page==0:
                                    sheet_name_target=sheet_name
                                else:
                                    sheet_name_target=f"""{sheet_name}_{self.page}"""
                                self.copy_sheet(sheet_name_target)
                                self.page+=1
                                #清楚明细表开始结束标记
                                if "row_start" in self.detail_field_dict:
                                    self.sheet_write(self.detail_field_dict["row_start"][0],self.detail_field_dict["row_start"][1],"")
                                if "row_end" in self.detail_field_dict:
                                    self.sheet_write(self.detail_field_dict["row_end"][0],self.detail_field_dict["row_end"][1],"")
                                #写主表数据
                                for filed in sheet_data:
                                    if filed in self.field_dict and type(self.field_dict[filed]) == list:
                                        for pos in self.field_dict[filed]:
                                            self.sheet_write(pos[0],pos[1],sheet_data[filed])
                            #开始写明细行数据
                            for detail_field in row_dict:
                                if detail_field in self.detail_field_dict:
                                    for pos in self.detail_field_dict[detail_field]:
                                        try:
                                            style=self.get_style(pos[0]+int(self.cur_row%self.row_range),pos[1])
                                        except:
                                            style=self.get_style(pos[0],pos[1])
                                        self.ws.write(pos[0]+int(self.cur_row%self.row_range),pos[1],row_dict[detail_field],style)
                                        # self.ws.write(pos[0]+int(self.cur_row%self.row_range),pos[1],row_dict[detail_field])
                                else:
                                    pass
                                    # print(cur_row,f"模板中{filed}.{detail_field}未指定")
                            self.cur_row+=self.row_row
                else:
                    # print(f"模板中{filed}未指定")
                    pass
            #2-不带明细数据的输出
            if not with_detail:
                self.copy_sheet(sheet_name)
                for filed in sheet_data:
                    if filed in self.field_dict and type(self.field_dict[filed]) == list:
                        for pos in self.field_dict[filed]:
                            self.sheet_write(pos[0],pos[1],sheet_data[filed])

        self.wb_save()

if __name__=="__main__":
    file_name="example.xls"
    example_sheet="Sheet1"
    print_data={"test":{'test2':"ddd", 'test1': "BBB","d1":[{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1},{"orderno":2,"sales":1}]}}
    dt1=[]
    for i in range(1,120):
        dt1.append({"orderno":f"A{i}","sales":f"B{i}"})
    print_data["test"]["d1"]=dt1
    class TEST_Template(Excel_Template):
        #template_file-模板文件,template_sheet-模板sheet,del_template-是否需要
        def __init__(self,template_file,template_sheet,del_template=True):
            self.template_file=template_file
            self.template_sheet=template_sheet
            self.del_template=del_template

        def end_process(self):
            pass
            # for worksheet in self.wb._Workbook__worksheets:
            #     worksheet.insert_bitmap('100year.bmp',1,4)

    print("开始输出")
    test=TEST_Template(template_file="example.xls",template_sheet="Sheet1")
    test.print_excel_with_template(save_name="test3.xls",print_data=print_data)
