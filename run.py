import pandas as pd
from Parse_KML import read_name_and_latlng
from algorithm import main_program
# import datetime

# 读取厂区信息与cdump信息
# print(datetime.datetime.now())
company_info_list = read_name_and_latlng('./shp&kml/临海工业园区.kml')
cdump_df = pd.read_csv('test.txt', sep='\s+', header=None,
                       names=['lat', 'lon', 'cdump'])

# 计算输出
company_contribution_dict_list = main_program(company_info_list, cdump_df)
print(company_contribution_dict_list)
# print(datetime.datetime.now())
