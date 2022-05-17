
library('tidyverse')
matches <- readr::read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-11-30/matches.csv')

## inspect the data
str(matches)

## preview the data
view(matches)

## MOST COMMON DPLYR FUNCTIONS
## select(): subset columns. To select all columns except certain ones, put a “-” in front of the variable to exclude it.
## filter(): subset rows on conditions
## mutate(): create new columns by using information from other columns
## group_by() and summarize(): create summary statistics on grouped data
## arrange(): sort results
## count(): count discrete values

## select(matches, winner, ground_country, match_date)
## filter(matches, winner == 'India')

## Combining above two statements
## select(filter(matches, winner == 'India'), winner, ground_country, match_date)
## or using pipe
## filter(matches, winner == 'India') %>% select(winner, ground_country, match_date)


select(matches, winner, ground_country, match_date) %>%
 group_by(winner) %>%
  summarize(wins = n()) %>% 
    filter(wins>1) %>%
    filter(winner != 'No result') %>%
    arrange(desc(wins)) %>% 
ggplot(aes(y=reorder(winner, -wins), x=wins)) + 
    geom_bar(stat="identity", fill="steelblue") +
    geom_text(aes(label = wins), hjust = -0.1) +
labs(
    title = 'ESPN Cricinfo Stats 1996',
    subtitle = 'Comparing Team Performance', 
    x = '# of Matches Won', 
    y = 'Winning Team',
    caption = '#30DayChartChallenge-2022-04-03 and #TidyTuesday-2021-11-30 @ parashar.ca'
) + 
theme(
    plot.title = element_text(color="maroon", size=24, face="bold.italic"),
    plot.subtitle = element_text(color="lightcoral", size=20, face="bold.italic"),
    axis.title.x = element_text(color="steelblue", size=16, face="bold"),
    axis.title.y = element_text(color="steelblue", size=16, face="bold"),
    plot.caption = element_text(color="slategrey", size=12, face="bold.italic")
)
ggsave("C:/Users/vivek/Documents/Code/Challenges-and-Competitions/30DayChartChallenge/output/2022-04-03.jpg")

