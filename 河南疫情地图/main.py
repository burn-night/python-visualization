"""
河南疫情地图
"""
import json
from pyecharts.charts import Map
from pyecharts.options import TitleOpts, VisualMapOpts

# 读取文件

f = open("D:/可视化案例数据/地图数据/疫情.txt", "r", encoding="UTF-8")
data = f.read()
# 关闭文件
f.close()
# 获取河南省数据
# json数据转换为python字典
data_dict = json.loads(data)
# 取河南省各市数据
cities_data = data_dict["areaTree"][0]["children"][3]["children"]
# 准备数据为元组并放入list
data_list = []
for city_data in cities_data:
    city_name = city_data["name"]+"市"
    city_confirm = city_data["total"]["confirm"]
    data_list.append((city_name, city_confirm))

# 手动添加济源市数据
data_list.append(("济源市", 5))

# 构建地图
map = Map()
map.add("河南省疫情分布", data_list, "河南")
# 设置全局选项
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
# 绘图9
map.render("河南疫情地图.html")