
import pandas as pd 
shelters = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-12-01/shelters.csv')

s=shelters.iloc[:5,:]

s.shelter_city.str.upper() # lower, strip, startswith('char'), endswith, get_dummies, len, 
s.shelter_address.str.split(' ', expand=True) # with expand=True, returns a df, else a list
s.shelter_address.str.split(' ').str[1]

s2=s.shelter_address.str.split(' ', expand=True)
s2.iloc[:,1].str.cat(s2.iloc[:,2], sep=', ')
# col1.str.cat(col2, sep=', ')

