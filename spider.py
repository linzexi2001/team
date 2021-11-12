from pyecharts.charts import *
from pyecharts.components import Table
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
import random
import datetime
from pyecharts.globals import CurrentConfig

CurrentConfig.ONLINE_HOST = "https://cdn.kesci.com/lib/pyecharts_assets/"

x_data = ['Apple', 'Huawei', 'Xiaomi', 'Oppo', 'Vivo', 'Meizu']
y_data = [123, 153, 89, 107, 98, 23]


bar = (Bar()
       .add_xaxis(x_data)
       .add_yaxis('', y_data)
      )
bar.render()