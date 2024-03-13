"""
全国疫情可视化地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import *

# 读取文件
f = open("D:/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()  # 读取全部数据

# 取到各省数据
# 将字符串json转为python的字典
data_dict = json.loads(data)  # 基础数据字典
# 从字典取出各省数据
province_data_list = data_dict["areaTree"][0]["children"]
# 组装每个省份和确诊人数为元组，并将每个省的数据都封装入列表内
data_list = []
for province_data in province_data_list:
    if province_data["name"] == "内蒙古":
        province_name = province_data["name"] + "自治区"
    elif province_data["name"] == "新疆":
        province_name = province_data["name"] + "维吾尔自治区"
    elif province_data["name"] == "西藏":
        province_name = province_data["name"] + "自治区"
    else:
        province_name = province_data["name"] + "省"
    province_confirm = province_data["total"]["confirm"]
    data_list.append((province_name, province_confirm))
# 创建地图对象
map = Map()
# 添加数据
map.add("各省确诊人数", data_list, "china")
# 设置全局配置，定制分段的视觉映射
map.set_global_opts(
    title_opts=TitleOpts(title="全国疫情地图"),
    visualmap_opts=VisualMapOpts(
        is_show=True,  # 是否显示
        is_piecewise=True,  # 是否分级
        pieces=[
            {"min": 1, "max": 99, "lable": "1~99人", "color": "#CCFFFF"},
            {"min": 100, "max": 999, "lable": "100~999人", "color": "#FFFF99"},
            {"min": 1000, "max": 9999, "lable": "1000~9999人", "color": "#FF9966"},
            {"min": 10000, "max": 99999, "lable": "10000~99999人", "color": "#FF6666"},
            {"min": 100000, "max": 999999, "lable": "100000~999999人", "color": "#CC3333"},
            {"min": 1000000, "lable": "1~99人", "color": "#990033"},
        ]
    )

)
# 绘图
map.render("全国疫情地图.html")
# 关闭文件
f.close()
