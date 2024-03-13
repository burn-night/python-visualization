import json
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LabelOpts

# 处理数据
# 读取美国的全部数据
f_us = open("D:/可视化案例数据/折线图数据/美国.txt", "r", encoding="UTF-8")
us_data = f_us.read()
# 读取日本的全部数据
f_jp = open("D:/可视化案例数据/折线图数据/日本.txt", "r", encoding="UTF-8")
jp_data = f_jp.read()
# 读取印度的全部数据
f_in = open("D:/可视化案例数据/折线图数据/印度.txt", "r", encoding="UTF-8")
in_data = f_in.read()
# 去掉不合JSON规范的开头
us_data = us_data.replace("jsonp_1629344292311_69436(", "")
jp_data = jp_data.replace("jsonp_1629350871167_29498(", "")
in_data = in_data.replace("jsonp_1629350745930_63180(", "")
# 去掉不合JSON规范的结尾
us_data = us_data[:-2]
jp_data = jp_data[:-2]
in_data = in_data[:-2]
# JSON转Python字典
us_dict = json.loads(us_data)
jp_dict = json.loads(jp_data)
in_dict = json.loads(in_data)

# 获取trend key
us_trend_data = us_dict['data'][0]['trend']
jp_trend_data = jp_dict['data'][0]['trend']
in_trend_data = in_dict['data'][0]['trend']

# 获取日期数据，用于x轴，取2020年（到314下标结束）
us_x_data = us_trend_data['updateDate'][:314]

# 获取确认数据，用于y轴，取2020年（到314下标结束）
us_y_data = us_trend_data['list'][0]['data'][:314]
jp_y_data = jp_trend_data['list'][0]['data'][:314]
in_y_data = in_trend_data['list'][0]['data'][:314]

# 生成图表
# 创建折线图对象
line = Line()
# 给折线图对象添加X轴
line.add_xaxis(us_x_data)
# 4：给折线图对象添加y轴
line.add_yaxis("美国确诊人数", us_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("日本确诊人数", jp_y_data, label_opts=LabelOpts(is_show=False))
line.add_yaxis("印度确诊人数", in_y_data, label_opts=LabelOpts(is_show=False))
# 设置全局配置项set_global_opts来设置
line.set_global_opts(
    title_opts=TitleOpts(title="2022年美日印确诊人数", pos_left="center", pos_bottom="1%"),
)

# 生成图表
line.render()

# 关闭文件
f_us.close()
f_jp.close()
f_in.close()
