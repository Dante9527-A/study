import requests
import re
import json

# 爬虫程序
class DingXiangSpider:
    def __init__(self):
        self.__url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia?from=singlemessage&isappinstalled=0'
        self.__headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'}

    def get_data(self):
        """从响应内容中提取包含所抓数据的json"""
        html = requests.get(url=self.__url, headers=self.__headers).content.decode('utf-8', 'ignore')
        regex = "window.getAreaStat = (.*?)catch\(e\)"
        pattern = re.compile(regex, re.S)
        str_data_list = pattern.findall(html)
        str_data = str_data_list[0][:-1] if str_data_list else None
        if str_data:
            return self.__get_json_data(str_data)

    def __get_json_data(self, str_data):
        """转为json数据，并提取所需数据"""
        json_data = json.loads(str_data)
        province_list = []
        for one_province_dict in json_data:
            province_name = self.__format_province(one_province_dict['provinceName'])
            one_province_info = [province_name, one_province_dict['confirmedCount']]
            province_list.append(one_province_info)
        return province_list

    def __format_province(self, name: str):
        if name.endswith("省") or name.endswith("市"):
            return name[:-1]
        elif name == "内蒙古自治区":
            return "内蒙古"
        elif name.endswith("自治区"):
            return name[:2]
        elif name.endswith("行政区"):
            return name[:2]
        return name

spider = DingXiangSpider()
data = spider.get_data()
print(data)
# 20200212
# [['湖北', 64084], ['广东', 1342], ['浙江', 1205], ['山东', 754], ['河南', 1271], ['安徽', 989], ['江西', 934], ['湖南', 1016], ['四川', 526], ['黑龙江', 480], ['重庆', 573], ['江苏', 631], ['北京', 399], ['广西', 249], ['福建', 293], ['河北', 311], ['陕西', 245], ['上海', 335], ['天津', 135], ['海南', 168], ['云南', 174], ['香港', 70], ['贵州', 146], ['辽宁', 121], ['山西', 132], ['内蒙古', 75], ['新疆', 76], ['吉林', 91], ['台湾', 26], ['宁夏', 71], ['甘肃', 91], ['澳门', 10], ['青海', 18], ['西藏', 1]]
