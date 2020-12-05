
#directory <-getwd()
tuesdata <- tidytuesdayR::tt_load('2020-11-24')
hike_data <- tuesdata$hike_data
hike_data <- within(hike_data, rm(features))
write.csv(hike_data, '/Users/vivekparashar/OneDrive/OneDrive-GitHub/Challenges-and-Competitions/TidyTuesday/Data/2020-11-24/hike_data.csv')


# practicing tidyverse
library(tidyverse)
tidyverse_conflicts()


# functions dplyr offers:
    select(): Select columns from your dataset
    filter(): Filter out certain rows that meet your criteria(s)
    group_by(): Group different observations together such that the original dataset does not change. Only the way it is represented is changed in the form of a list
    summarise(): Summarise any of the above functions
    arrange(): Arrange your column data in ascending or descending order
    join(): Perform left, right, full, and inner joins in R
    mutate(): Create new columns by preserving the existing variables

hike_data %>% summary()
hike_data %>% summarise(meangain = mean(as.numeric(gain))) # median, mode, 
hike_data %>% filter(rating>4)
hike_data %>% arrange(desc(name))
hike_data %>% mutate()
hike_data %>% group_by(location) %>% summarize (meangain = mean(as.numeric(gain)))
joined_data <- left_join(data,fc,by="center_id")

as.numeric(unlist(strsplit(hike_data$length[1],' '))[1])


# converting between vector types
# as.character(), as.numeric, factor, unclass(f), as.integer()

# colnames(hike_data)

# class(x) returns the variable type
# as.integer() function can be used to convert a number into integer type


# conditional statements
x %>% mutate(col1 = ifelse(col1 == 0, "No", "Yes"))


# String manipulation
nchar(x)
toupper(x)
tolower(x)
substr(x, start, stop)
# grep() function searches for a pattern inside a given string and returns the number of instances a match is found
grep(pattern, x, ignore.case = FALSE, perl = FALSE, value = FALSE, fixed = FALSE, useBytes = FALSE, invert = FALSE)
# paste() function converts objects into characters and concatenates them
paste("hello", "world", "!", sep = "-")
# strsplit() function splits the given input string into substrings according to the given split argument
strsplit(x, split, fixed = FALSE, perl = FALSE, useBytes = FALSE)
# sprintf() function prints strings with variables in them
sprintf("There are %d dollars in %s's %s", count, name, place)
# cat() function combines all input objects into a single character vector
cat("hello","this","is","Techvidvan",sep = "-")
# sub() function replaces the first occurrence of a substring in a string with another substring
sub(old, new, string)
sub("My Name Is", "I Am", string)

# functions that you can perform with the stringr package are:
    str_sub(): Extract substrings from a character vector
    str_trim():Trim white spaces
    str_length(): Checks the length of the string
    str_to_lower/str_to_upper: Converts the string into upper case or lower case


Indexing Vectors
    x[n] nth element
    x[-n] all but the nth element
    x[1:n] first n elements
    x[-(1:n)] elements from n+1 to the end
    x[c(1,4,2)] specific elements
    x[“name”] element named “name”
    x[x > 3] all elements greater than 3
    x[x > 3 & x < 5] all elements between 3 and 5
    x[x %in% c(“a”,”and”,”the”)] elements in the given set

Indexing Lists
    x[n] list with elements n
    x[[n]] nth element of the list
    x[[“name”]] element of the list named “name”


# pivot longer and pivot wider
# functions tidyr offers:
    gather(): The function “gathers” multiple columns from your dataset and converts them into key-value pairs
    spread(): This takes two columns and “spreads” them into multiple columns
    separate(): As the name suggests, this function helps in separating or splitting a single column into numerous columns
    unite(): Works completely opposite to the separate() function. It helps in combining two or more columns into one

# Reshape in R from wide to long and from long to wide
# create data frame
country<-data.frame(c("A","B","C"),c(100,200,120),c(2000,7000,15000))
colnames(country)<- c("countries","population_in_million","gdp_percapita")

# wide to long and long to wide using reshape
## reshape in R from wide to long example
country_w_to_L<- reshape(data=country, idvar="countries",
    varying = c("population_in_million","gdp_percapita"),
    v.name=c("value"),
    times=c("population_in_million","gdp_percapita"),
    new.row.names = 1:1000,
    direction="long")	 
## reshape in R from long to wide example
country_L_to_w <- reshape(data=country_w_to_L,idvar="countries",
    v.names = "value",
    timevar = "time",
    direction="wide")

# tidyr approach - wide to long using gather and long to wide using spread 
library(tidyr)
data_long = gather(country, detail, value, population_in_million:gdp_percapita, factor_key=TRUE)
data_wide = spread(data_long, detail, value)

# Wide to long using melt() function in R
library(reshape)
country_w_to_L = melt(country, id.vars=c("countries"))
# long to wide using cast function of reshape2() package in R 
library(reshape2)
country_L_to_W = dcast(country_w_to_L, countries~variable,sum) 
	

# Plotting 
library(ggplot2)
# Plot barplot of rating
ggplot(hike_data, aes(x = rating, fill=var)) + # fill = var will show stacked bar
  geom_bar()

# Scatter plot of highpoint vs rating
ggplot(hike_data %>% drop_na(), aes(x = highpoint, y = rating)) +
  geom_point() +
  #facet_grid(~var) # shows multiple charts with different values of var 

# scatter plot - another example
ggplot(data = data) +
  aes(x = checkout_price, y = base_price) +
  geom_point(color = "#1f9e89") +
  theme_minimal()
  
# density chart
ggplot(data = data) +
  aes(x = num_orders) +
  geom_density(adjust = 1, fill = "#0c4c8a") +
  theme_minimal()

# violin plot
ggplot(data = data) +
  aes(x = num_orders, y = num_orders) +
  geom_violin(scale = "area", adjust = 1, fill = "#0c4c8a") +
  theme_minimal()


# readr
read_delim("filename.csv",delim=",")
# readxl
data <- read_xlsx("filename.xlxs")
# haven: For importing SPSS, STATA and SAS data
dat = read_sas("path to file", "path to formats catalog")


# Tibble is a type of dataframe in R. It truly stands out when we’re trying to detect anomalies in our dataset. How? Tibble does not change variable names or types. It certainly doesn’t throw up errors when a variable does not exist or a value is missing.
data<- as.tibble(train)

# purrr package in R provides a complete toolkit for enhancing R’s functional programming. We can use the functions provided by purrr to avoid many loops with just one line of code.
map_dbl(train,~mean(.x)) # mean of every column in your data

# lubridate provides a series of functions that are a permutation of the letters “m”, “d” and “y” to represent the ordering of month, day and year
dates <- c("January 11,2019" , "September 12, 2018", "April 1, 2019")
dates <- mdy(dates)

# hms: This packages works similar to lubridate but only with time-based variables
x <- c("09:10:01", "09:10:02", "09:10:03")
hms(x)



