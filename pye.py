from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"


data = [[[28604, 77, 17096869, 'Australia', 1990],
         [31163, 77.4, 27662440, 'Canada', 1990],
         [1516, 68, 1154605773, 'China', 1990],
         [13670, 74.7, 10582082, 'Cuba', 1990],
         [28599, 75, 4986705, 'Finland', 1990],
         [29476, 77.1, 56943299, 'France', 1990],
         [31476, 75.4, 78958237, 'Germany', 1990],
         [28666, 78.1, 254830, 'Iceland', 1990],
         [1777, 57.7, 870601776, 'India', 1990],
         [29550, 79.1, 122249285, 'Japan', 1990],
         [2076, 67.9, 20194354, 'North Korea', 1990],
         [12087, 72, 42972254, 'South Korea', 1990],
         [24021, 75.4, 3397534, 'New Zealand', 1990],
         [43296, 76.8, 4240375, 'Norway', 1990],
         [10088, 70.8, 38195258, 'Poland', 1990],
         [19349, 69.6, 147568552, 'Russia', 1990],
         [10670, 67.3, 53994605, 'Turkey', 1990],
         [26424, 75.7, 57110117, 'United Kingdom', 1990],
         [37062, 75.4, 252847810, 'United States', 1990]],
        [[44056, 81.8, 23968973, 'Australia', 2015],
         [43294, 81.7, 35939927, 'Canada', 2015],
         [13334, 76.9, 1376048943, 'China', 2015],
         [21291, 78.5, 11389562, 'Cuba', 2015],
         [38923, 80.8, 5503457, 'Finland', 2015],
         [37599, 81.9, 64395345, 'France', 2015],
         [44053, 81.1, 80688545, 'Germany', 2015],
         [42182, 82.8, 329425, 'Iceland', 2015],
         [5903, 66.8, 1311050527, 'India', 2015],
         [36162, 83.5, 126573481, 'Japan', 2015],
         [1390, 71.4, 25155317, 'North Korea', 2015],
         [34644, 80.7, 50293439, 'South Korea', 2015],
         [34186, 80.6, 4528526, 'New Zealand', 2015],
         [64304, 81.6, 5210967, 'Norway', 2015],
         [24787, 77.3, 38611794, 'Poland', 2015],
         [23038, 73.13, 143456918, 'Russia', 2015],
         [19360, 76.5, 78665830, 'Turkey', 2015],
         [38225, 81.4, 64715810, 'United Kingdom', 2015],
         [53354, 79.1, 321773631, 'United States', 2015]]]
tool_js = """function (param) {return param.seriesName + ' — ' +param.data[3]+'<br/>' 
            +'人均GDP： '+param.data[0]+' 美元<br/>'
            +'GDP总量： '+param.data[2]+' 美元<br/>'
            +'人均寿命： '+param.data[1]+'岁';}"""


item_color_js_1 = """new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(251, 118, 123)'
            }, {
                offset: 1,
                color: 'rgb(204, 46, 72)'
            }])"""

item_color_js_2 = """new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                offset: 0,
                color: 'rgb(129, 227, 238)'
            }, {
                offset: 1,
                color: 'rgb(25, 183, 207)'
            }])"""

symbol_js = """function (data) {return Math.sqrt(data[2]) / 5e2;}"""

item_style_1 = {
    'shadowBlur': 10,
    'shadowColor': 'rgba(120, 36, 50, 0.5)',
    'shadowOffsetY': 5,
    'color': JsCode(item_color_js_1)
}

item_style_2 = {
    'shadowBlur': 10,
    'shadowColor': 'rgba(120, 36, 50, 0.5)',
    'shadowOffsetY': 5,
    'color': JsCode(item_color_js_2)
}

bg_color_js = """
new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
        offset: 0,
        color: '#f7f8fa'
    }, {
        offset: 1,
        color: '#cdd0d5'
    }])"""

scatter1 = (Scatter(init_opts=opts.InitOpts(bg_color=JsCode(bg_color_js),width='1000px', height='800px'))
            .add_xaxis([i[0] for i in data[0]])
            .add_yaxis("1990年", [[i[1], i[2], i[3]] for i in data[0]],
                       symbol_size=JsCode(symbol_js),
                       label_opts=opts.LabelOpts(is_show=False),
                       itemstyle_opts=item_style_1)
            .set_global_opts(yaxis_opts=opts.AxisOpts(name='人均寿命', type_="value", is_scale=True,
                                                     splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(type_='dashed'))),
                             xaxis_opts=opts.AxisOpts(name='人均GDP', type_="value",
                                                     splitline_opts=opts.SplitLineOpts(is_show=True, linestyle_opts=opts.LineStyleOpts(type_='dashed'))),
                             tooltip_opts=opts.TooltipOpts(formatter=JsCode(tool_js)),
                             legend_opts=opts.LegendOpts(is_show=True, pos_right=10),
                             title_opts=opts.TitleOpts(title="1990 与 2015 年各国家人均寿命与 GDP"))
            )


scatter2 = (Scatter()
            .add_xaxis([i[0] for i in data[1]])
            .add_yaxis("2015年", [[i[1], i[2], i[3]] for i in data[1]],
                       symbol_size=JsCode(symbol_js),
                       label_opts=opts.LabelOpts(is_show=False),
                       itemstyle_opts=item_style_2)
            )


scatter1.overlap(scatter2)
scatter1.render()