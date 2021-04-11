
import pandas as pd
import altair as alt

office_ratings = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-17/office_ratings.csv')

#alt.data_transformers.disable_max_rows()
chart = alt.Chart(office_ratings).mark_tick().encode(
    #x='imdb_rating:Q',
    alt.X('imdb_rating:Q',
        scale=alt.Scale(domain=(6, 10)),
        axis=alt.Axis(title='IMDb Rating') #(format='%', title='percentage')
    ),
    alt.Y('season:O',
        axis=alt.Axis(title='Season') 
    )
).properties(
    #width=550, height=140, 
    title={
      "text": ['The Office IMDb Ratings Distribution by Season'], 
      "fontSize": 18,
      "font": 'Courier',
      "anchor": 'middle',
      "color": 'gray'
    }
)
alt.concat(chart, 
    title=alt.TitleParams(
        ['', '#30DayChartChallenge - strips - 2021/04/12', 
        'Dataset: TidyTuesday Dataset 2020-03-17', 
        'twitter.com/vivekparasharr | github.com/vivekparasharr | vivekparasharr.medium.com'],
        baseline='bottom',
        orient='bottom',
        anchor='end',
        fontWeight='normal',
        fontSize=12,
        color='gray'
    )
)

