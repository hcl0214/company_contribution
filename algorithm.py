import pandas as pd
from Parse_KML import read_name_and_latlng
from PNPoly import if_points_in_polygon

# 预处理


def pretreatment(one_company_info_dict, cdump_df):
    return_info_dict = {'name': one_company_info_dict['name'], 'latlng': [
        (one_company_info_dict['lat'][i], one_company_info_dict['lon'][i]) for i in range(len(one_company_info_dict['lat']))]}
    lat_min = min(one_company_info_dict['lat'])
    lat_max = max(one_company_info_dict['lat'])
    lon_min = min(one_company_info_dict['lon'])
    lon_max = max(one_company_info_dict['lon'])
    valuable_df = cdump_df.query(
        f'{lat_min} < lat < {lat_max} and {lon_min} < lon < {lon_max}')
    return_valuable_df = valuable_df.groupby(['lat', 'lon']).sum()
    return return_info_dict, return_valuable_df

# 点位判断


def determine_points(company_info_dict, valuable_df):
    valuable_points_values = []
    for points_num in range(len(valuable_df)):
        point_lat = valuable_df.index[points_num][0]
        point_lon = valuable_df.index[points_num][1]
        point_value = valuable_df['cdump'][points_num]
        boundary_points = company_info_dict['latlng']
        valuable_value = if_points_in_polygon(
            point_lat, point_lon, point_value, boundary_points)
        valuable_points_values = [*valuable_points_values, valuable_value]
    company_contribution = sum(valuable_points_values)
    return company_contribution

# 后处理


def postprocess(company_info_dict, contribution_float):
    company_contribution_dict = {
        'name': company_info_dict['name'], 'contribution': contribution_float}
    return company_contribution_dict

# 主程序


def main_program(company_info_list, cdump_df):
    contributions_list = []
    for company_info in company_info_list:
        reshape_info_dict = pretreatment(company_info, cdump_df)[0]
        used_df = pretreatment(company_info, cdump_df)[1]
        # print(reshape_info_dict,used_df)
        company_contribution = determine_points(reshape_info_dict, used_df)
        company_contribution_dict = postprocess(
            company_info, company_contribution)
        contributions_list = [*contributions_list, company_contribution_dict]
    return contributions_list


if __name__ == '__main__':
    company_info_list = read_name_and_latlng('./shp&kml/临海工业园区.kml')
    cdump_df = pd.read_csv('test.txt', sep='\s+',
                           header=None, names=['lat', 'lon', 'cdump'])
    result = main_program(company_info_list, cdump_df)
    print(result)
