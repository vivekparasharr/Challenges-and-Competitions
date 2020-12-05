
import pandas as pd 

# Librdata, the C backend of pyreadr absolutely needs a file in disk and only a string with the path can be passed as argument, 
# therefore you cannot pass an url to pyreadr.read_r.
import pyreadr
url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-11-24/hike_data.rds?raw=True"
dst_path = "/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.rds"
res = pyreadr.read_r('/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.rds')
pyreadr.download_file(url, dst_path)


