
import numpy as np
import pandas as pd
import plotly.express as px

plastic = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-01-26/plastics.csv')

plastic[plastic.year==2019][plastic.parent_company.isin(['Grand Total','The Coca-Cola Company'])]

