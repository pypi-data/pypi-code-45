#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################
#                                                           
# Copyright (C)2018 SenseDeal AI, Inc. All Rights Reserved  
#                                                           
############################################################

'''                                                       
File: .py
Author: xuwei                                        
Email: weix@sensedeal.ai                                 
Last modified: 2018.12.20 18:25 
Description:                                            
'''

import json
import datetime
from sense_data.dictobj import *
from sense_data import stock_pb2
from sense_data.decorator import catch_except_log


def _dict_list_model(list_dict, model_class):
    if None:
        _obj = model_class(list_dict[0])
        return _obj
    _dct_list = []
    for _dct in list_dict:
        _dct_list.append(model_class(_dct))

    return _dct_list


class SenseDataService(object):

    def __init__(self):
        pass

    # 1
    @catch_except_log
    def get_stock_price_tick(self, stock_code, stub=None):
        _response = stub.get_stock_price_tick(stock_pb2.Request(stock_code=stock_code))
        _result = json.loads(_response.txt)
        _result = StockPriceTickObj(_result)
        return _result

    # 2
    @catch_except_log
    def get_company_info(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_company_info(stock_pb2.Request(stock_code=_stock_code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, CompanyInfoObj)
        if type(code) == str or len(code) == 1:
            return _dct_list[0]
        else:
            return _dct_list

    # 3
    @catch_except_log
    def get_company_alias(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_company_alias(stock_pb2.Request(stock_code=_stock_code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, CompanyAliasObj)
        return _dct_list

    # 4
    @catch_except_log
    def get_stock_price_day(self, *args, stub=None):
        if len(args) == 3:
            _response = stub.get_stock_price_day(
                stock_pb2.Request(var_num=len(args), stock_code=args[0], start_date=args[1], end_date=args[2]))
        elif len(args) == 2:
            _response = stub.get_stock_price_day(
                stock_pb2.Request(var_num=len(args), stock_code=args[0], start_date=args[1]))
        else:
            _response = stub.get_stock_price_day(
                stock_pb2.Request(var_num=len(args), stock_code=args[0]))

        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, StockPriceDayObj)
        if len(args) == 2:
            return _dct_list[0]
        else:
            return _dct_list

    # 5
    @catch_except_log
    def get_subcompany(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_subcompany(stock_pb2.Request(stock_code=_stock_code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, SubcompanyInfoObj)
        return _dct_list

    # 6
    @catch_except_log
    def get_industry_concept(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_industry_concept(stock_pb2.Request(stock_code=_stock_code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, IndustryConceptObj)
        if type(code) == str or len(code) == 1:
            return _dct_list[0]
        else:
            return _dct_list

    # 7
    @catch_except_log
    def get_chairman_supervisor(self, *args, stub=None):
        if len(args) == 2:
            _response = stub.get_chairman_supervisor(
                stock_pb2.Request(var_num=len(args), stock_code=args[0], post=args[1]))
        else:
            _response = stub.get_chairman_supervisor(
                stock_pb2.Request(var_num=len(args), stock_code=args[0]))

        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, ChairmanSupervisorObj)
        return _dct_list

    # 8
    @catch_except_log
    def get_stockholder(self, code, stub=None):
        _response = stub.get_stockholder(stock_pb2.Request(stock_code=code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, StockHolderObj)
        return _dct_list

    # 9
    @catch_except_log
    def get_trade_date(self, stub=None):
        _date_time_now = datetime.datetime.now()
        _time_str = _date_time_now.strftime("%Y-%m-%d")
        _response = stub.get_trade_date(stock_pb2.Request(time_str=_time_str))
        _time_str = json.loads(_response.trade_date) + ' 09:30:00'
        _time = datetime.datetime.strptime(_time_str, "%Y-%m-%d %H:%M:%S")
        _result = round(_time.timestamp())
        return _result

    # 10
    @catch_except_log
    def get_market_rise_fall(self, stub=None):
        _response = stub.get_market_rise_fall(stock_pb2.Request())
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, MarketDataObj)
        return _dct_list

    # 11
    @catch_except_log
    def get_industry_rise_fall(self, stub=None):
        _response = stub.get_industry_rise_fall(stock_pb2.Request())
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, IndustryDataObj)
        return _dct_list

    # 12
    @catch_except_log
    def get_concept_rise_fall(self, stub=None):
        _response = stub.get_concept_rise_fall(stock_pb2.Request())
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, ConceptDataObj)
        return _dct_list

    # 13
    @catch_except_log
    def get_entity_role(self, entity, stub=None):
        _response = stub.get_entity_role(stock_pb2.Request(entity_name=entity))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, EntityRoleObj)
        return _dct_list

    # 14
    @catch_except_log
    def get_financial_info(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_financial_info(stock_pb2.Request(stock_code=_stock_code))
        _list = json.loads(_response.txt)
        _dct_list = _dict_list_model(_list, FinancialInfoObj)
        if type(code) == str or len(code) == 1:
            return _dct_list[0]
        else:
            return _dct_list

    # 15子龙用
    @catch_except_log
    def get_total_shares(self, code, stub=None):
        _company_code = json.dumps(code)
        _response = stub.get_total_shares(stock_pb2.Request(company_code=_company_code))
        return json.loads(_response.txt)

    # 16子龙用
    @catch_except_log
    def get_company_name(self, stub=None):
        _response = stub.get_company_name(stock_pb2.Request())
        return json.loads(_response.txt)

    # 17广彬用
    @catch_except_log
    def get_title_code(self, title, stub=None):
        _response = stub.get_title_code(stock_pb2.Request(title=title))
        _result_list = eval(_response.txt)
        return _result_list

    # 18子龙用
    @catch_except_log
    def get_actual_control_person(self, code, stub=None):
        _stock_code = json.dumps(code)
        _response = stub.get_actual_control_person(stock_pb2.Request(stock_code=_stock_code))
        _result_list = json.loads(_response.txt)
        if type(code) == str or len(code) == 1:
            return _result_list[0]
        else:
            return _result_list

    # 19徐威用
    @catch_except_log
    def get_code_by_name(self, name, stub=None):
        _response = stub.get_code_by_name(stock_pb2.Request(entity_name=name))
        return json.loads(_response.txt)

    # 20徐威用
    @catch_except_log
    def get_origin_info_by_name(self, name, stub=None):
        _response = stub.get_code_by_name(stock_pb2.Request(entity_name=name))
        return json.loads(_response.txt)

    # 21广彬用
    @catch_except_log
    def get_detail_info_by_name(self, name, stub=None):
        _response = stub.get_detail_info_by_name(stock_pb2.Request(entity_name=name))
        return json.loads(_response.txt)

    # 22广彬用
    @catch_except_log
    def get_company_role_info(self, code, stub=None):
        _response = stub.get_company_role_info(stock_pb2.Request(stock_code=code))
        return json.loads(_response.txt)

    # 23于鑫用
    @catch_except_log
    def get_infos_by_terms(self, names_list: list, stub=None):
        _names_list = json.dumps(names_list, ensure_ascii=False)
        _response = stub.get_infos_by_terms(stock_pb2.Request(entity_name=_names_list))
        return json.loads(_response.txt)


if __name__ == '__main__':
    import sense_core as sd
    sd.log_init_config(root_path=sd.config('log_path'))
    sense_data = SenseDataService()
    r = sense_data.get_detail_info_by_name('石化油服')
    print(r)
