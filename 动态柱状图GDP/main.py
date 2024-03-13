"""
演示第三个图表：GDP动态柱状图开发
"""
from pyecharts.charts import Bar, Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType
# 读取数据
f = open("D:/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv", "r", encoding="GB2312")
data_lines = f.readlines()
# 关闭文件
f.close()
# 删除第一条数据
data_lines.pop(0)
# 将数据转换为字典存储，格式为：
# { 年份 ：[[国家， gdp], [国家，gdp], ......]}
data_dict = {}
for line in data_lines:
    year = int(line.split(",")[0])
    country = line.split(",")[1]
    gdp = float(line.split(",")[2])
    try:
        data_dict[year].append([country, gdp])
    except KeyError:
        data_dict[year] = []
        data_dict[year].append([country, gdp])
# 创建时间线对象
timeline = Timeline({"theme":ThemeType.LIGHT})

# 排序年份
sorted_year_list = sorted(data_dict.keys())
for year in sorted_year_list:
    data_dict[year].sort(key=lambda element: element[1], reverse=True)
    year_data = data_dict[year][0:8]
    x_data = []
    y_data = []
    # for循环每一年的数据，基于每一年的数据，创建每一年的bar对象
    # 在for循环中，将每一年的bar对象添加到时间线中
    for country_gdp in year_data:
        x_data.append(country_gdp[0])
        y_data.append(country_gdp[1]/100000000)

    bar = Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)
    bar.add_yaxis("GDP(亿)", y_data, label_opts=LabelOpts(position="right"))
    bar.reversal_axis()
    bar.set_global_opts(
        title_opts=TitleOpts(title=f"{year}年全球前八GDP数据")
                        )
    timeline.add(bar, str(year))

# 设置时间线自动播放
timeline.add_schema(
    play_interval=400,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=False
)
# 绘图
timeline.render("1960年~2019年全球GDP前八国家.html")