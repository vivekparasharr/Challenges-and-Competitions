
from matplotlib.pyplot import xticks
import numpy as np
import pandas as pd

water = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-04/water.csv')


from dataprep.eda import create_report
df = load_dataset("titanic")
create_report(df).show_browser()


