from pykml import parser


def read_name_and_latlng(filename: str):
    with open(f'{filename}', 'r', encoding="utf-8") as f:
        kml = parser.parse(f).getroot()

    info_dict_list = []
    for each in kml.Document.Folder.Placemark:
        # name
        company_name = each.name.text

        # latitude & longitude
        latlon = each.Polygon.outerBoundaryIs.LinearRing.coordinates
        latlon_str = latlon.text.replace(' ', '')
        latlon_list = latlon_str.split('\n')[1:-1]
        lon_list = [float(llh_str.split(',')[0]) for llh_str in latlon_list]
        lat_list = [float(llh_str.split(',')[1]) for llh_str in latlon_list]
        info_dict = {'name': company_name, 'lon': lon_list, 'lat': lat_list}
        info_dict_list = [*info_dict_list, info_dict]
        # print(info_dict_list)

    return info_dict_list


if __name__ == '__main__':
    company_info_list = read_name_and_latlng('./shp&kml/临海工业园区.kml')
    with open('company_info.txt', 'w') as fl:
        company_info_list = [f'{info}\n' for info in company_info_list]
        fl.writelines(company_info_list)
