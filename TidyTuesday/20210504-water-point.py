
from matplotlib.pyplot import xticks
import numpy as np
import pandas as pd

water = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-04/water.csv')


import dataprep.eda as eda
eda.create_report(water).show_browser()

eda.plot(water, 'water_source')
eda.plot(water, 'water_source', 'water_tech').show_browser()

eda.plot(water, 'water_source', 'country_name').show_browser()

