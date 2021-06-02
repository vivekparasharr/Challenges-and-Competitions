
import numpy as np
import pandas as pd
from pyecharts.charts import Pie
from pyecharts import options as opts

# Librdata, the C backend of pyreadr absolutely needs a file in disk and only a string with the path can be passed as argument, 
# therefore you cannot pass an url to pyreadr.read_r.
'''
import pyreadr # can be used to download rds file
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-24/hike_data.rds?raw=True"
dst_path = "/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.rds"
res = pyreadr.read_r('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.rds')
pyreadr.download_file(url, dst_path)
'''

df=pd.read_csv('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/trails_summary.csv')
df=df.sort_values('no_trails') #, ascending=False)

# Nightingale Rose Chart
c = df['region'].values.tolist()
d = df['no_trails'].values.tolist()#create the color_series for the rosechart
# define rosechart
rosechart = Pie(init_opts=opts.InitOpts(width='1350px', height='750px'))
# set the color
color_series = ['#802200','#B33000','#FF4500','#FAA327','#9ECB3C',
 '#6DBC49','#37B44E','#14ADCF','#209AC9','#1E91CA',
 '#2C6BA0','#2B55A1','#2D3D8E','#44388E','#6A368B',
 '#D02C2A','#D44C2D','#F57A34','#FA8F2F','#D99D21']
rosechart.set_colors(color_series)
# add the data to the rosechart
rosechart.add("", [list(z) for z in zip(c, d)],
        radius=["20%", "95%"],  # 20% inside radius，95% ourside radius
        center=["30%", "60%"],   # center of the chart
        rosetype="area")# set the global options for the chart
rosechart.set_global_opts(title_opts=opts.TitleOpts(title='Washington Trails',subtitle="# of Trails by Region"),
                     legend_opts=opts.LegendOpts(is_show=False),
                     toolbox_opts=opts.ToolboxOpts())# set the series options
rosechart.set_series_opts(label_opts=opts.LabelOpts(is_show=True, position="inside", font_size=12, formatter="{b}:{c}", font_style="italic",font_weight="bold", font_family="Century"),)
rosechart.render_notebook()
#rosechart.render(path='/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/washington-trails.png')
