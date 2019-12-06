import requests
import pandas as pd
import requests
import random 
import string

class agrud:
    def __init__(self,api_key,secret_key,base_url="https://www.marketanalyst.ai"):

        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

        self.N = 8

    def get_category_id(self,category_type):
        indicator_category_url = self.base_url + "/api_get_indicator_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(indicator_category_url, data=payload)
        indicator_category_data = response.json()
        if "data" not in indicator_category_data:
            return "api key or secret key is invalid"
        indicator_category_data = indicator_category_data['data']
        for category in indicator_category_data:
            if category["title"] == category_type:
                return int(category["id"])
        return "this category does not exsist"

    def get_categody_sub_id(self,indicator_id,sub_category_type):
        sub_category_type_url = self.base_url + "/api_get_indicator_sub_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'indicator_category_id': indicator_id}
        response = requests.post(sub_category_type_url, data=payload)
        sub_indicator_category_data = response.json()
        if "data" not in sub_indicator_category_data:
            return "api key or secret key is invalid"
        sub_indicator_category_data = sub_indicator_category_data['data']
        for sub_category in sub_indicator_category_data:
            if sub_category["title"] == sub_category_type:
                return int(sub_category["id"])
        return "this sub category does not exsist"
    
    def get_security_id(self,security_string):
        security_url = self.base_url + "/api_get_security"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(security_url, data=payload)
        security_data = response.json()
        if "data" not in security_data:
            return "api key or secret key is invalid"
        security_data = security_data['data']
        for security in security_data:
            if security["title"] == security_string:
                return int(security["id"])
        return "this security does not exsist"

    def download_data(self,security_exchange,start_date,end_date,category_type,sub_category_type):
        download_name = ''.join(random.choices(string.ascii_uppercase +string.digits, k = self.N))
        category_id = self.get_category_id(category_type)
        if type(category_id) != int:
            return category_id
        sub_category_id = self.get_categody_sub_id(category_id,sub_category_type)
        if type(sub_category_id) != int:
            return sub_category_id
        security_id = self.get_security_id(security_exchange)
        if type(security_id) != int:
            return security_id
        criteria_url = self.base_url + "/api_my_download"
        payload = {
            "api_key":self.api_key,
            "secret_key":self.secret_key,
            "time_period":"{'from_date':'" + str(start_date) + "','to_date':'" + str(end_date) + "'}",
            "download_name":download_name,
            "security":security_id,
            "indicator_category":category_id,
            "indicator_sub_category":sub_category_id,
            "formate":"json"
        }
        response = requests.post(criteria_url, data=payload)
        criteria_list_url = self.base_url + "/api_criteria_list"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        criteria_list_response = requests.post(criteria_list_url, data=payload)
        criteria_list_data = criteria_list_response.json()["data"]
        for temp_criteria in criteria_list_data:
            if temp_criteria["name"] == download_name:
                criteria_id = temp_criteria["id"]
        criteria_download_url =  self.base_url + "/api_my_criteria"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'criteria_id':criteria_id}
        criteria_download_response = requests.post(criteria_download_url, data=payload)
        return pd.DataFrame.from_dict(criteria_download_response.json())

    def get_close_price(self,security_exchange,start_date,end_date,category_type,sub_category_type,interval):
        df = self.download_data(security_exchange,start_date,end_date,category_type,sub_category_type)
        df1 = df[df["indicator"] == "D_EODCLOSE_EXT_1"].copy()
        df1['ma'] = df1['value'].rolling(interval).mean()
        return df1

