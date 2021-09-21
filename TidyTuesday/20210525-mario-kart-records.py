
import numpy as np
import pandas as pd
from matplotlib.pyplot import xticks
import dataprep.eda as eda

records = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv')
drivers = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/drivers.csv')

records.info()
records.head(5)

drivers.info()

