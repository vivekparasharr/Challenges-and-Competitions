
import numpy as np
import pandas as pd
from matplotlib.pyplot import xticks
import dataprep.eda as eda

records = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv')
drivers <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/drivers.csv')


broadband.columns=['ST', 'COUNTY_ID', 'COUNTY_NAME', 'AVAILABILITY', 'USAGE']

eda.create_report(records).show_browser()

eda.plot(survey[survey.annual_salary<1000000], 'annual_salary', 'industry').show_browser()
eda.plot(survey[survey.annual_salary<500000], 'annual_salary', 'industry').show_browser()

eda.plot(
    survey[survey.annual_salary<500000].replace(to_replace={
        '5-7 years':'05-07 years', '2 - 4 years':'02-04 years', 
        '21 - 30 years':'21-30 years', '11 - 20 years':'11-20 years',
        '1 year or less':'01 year or less', 
        '8 - 10 years':'08-10 years', '31 - 40 years':'31-40 years',
        '41 years or more':'41 years or more'
    }), 'annual_salary', 'years_of_experience_in_field').show_browser()

survey[survey.annual_salary<500000].years_of_experience_in_field.unique()
