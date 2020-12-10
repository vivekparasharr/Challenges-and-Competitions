
#directory <-getwd()
library(tidyverse)
library(stringr)
library(prismatic) # package to view colors in console output
prismatic::color(c('#6C5B7B', '#C06C89', '#F67280', '#F8B195'))

library(Cairo) # for export type
library(scales)
library(extrafont)
tidyverse_conflicts()

tuesdata <- tidytuesdayR::tt_load('2020-11-24')
hike_data <- tuesdata$hike_data

# extract region
hike_data$region <- word(hike_data$location, 1 , sep=' -- ')
hike_data$region <- as.factor(hike_data$region)

# extract miles
hike_data$length_num <- as.numeric(word(hike_data$length,1,sep=' '))
# as.numeric(sapply(strsplit(hike_data$length, ' '), '[[', 1))
# readr::parse_number(hike_data$length)

# convert everything to a numeric
hike_data$gain <- as.numeric(hike_data$gain)
hike_data$highpoint <- as.numeric(hike_data$highpoint)
hike_data$trackNr <- as.numeric(row.names(hike_data))

# convert to df
hike_data <- data.frame(hike_data)

# calculate commulative length and mean gain
summary_stats = hike_data %>% group_by(region) %>%
  summarize(sum_length=sum(length_num),
            mean_gain = mean(gain),
            #n = n() # counts every single row within the group by
            ) %>% 
            mutate(mean_gain = round(mean_gain, digits=0))

# cummulative nr of tracks  per region
trackNrs = hike_data %>% group_by(region) %>% count()

# join nr of tracks back to summary stats 
summary_all = left_join(summary_stats, trackNrs, by='region')

# visualize
# done in .py file

################## ideas not used #################

# unlist a list
unlist(hike_data$features[1])[6]
# remove columns from a df
hike_data <- within(hike_data, rm(features))
# write data to disk
write.csv(hike_data, '/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.csv')
