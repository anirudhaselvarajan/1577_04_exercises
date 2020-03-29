setwd("D:/Tiger@Me/Training/Takeaway Assignment - R _ Python")

# Import libraries
library(readxl)
library(dplyr)
library(lubridate)
library(readr)

# Define functions

# Q1 Find least sales amount for each item

least_sales <- function(df){
  # write code to return pandas dataframe
  print("Q1 Find least sales amount for each item")
  ls <- aggregate(df$Sale_amt, by = list(df$Item), function(x) min(x))
  return(ls)
}

# Q2 compute total sales at each year X region
sales_year_region <- function(df){
  # write code to return pandas dataframe
  print("Q2 compute total sales at each year X region")
  df['year'] <- year(SaleData$OrderDate)
  sales_year_region <- df %>%
    select(year,Region,Unit_price) %>%
    group_by(year,Region) %>%
    summarise(Unit_price= sum(Unit_price))
  return(sales_year_region)
}

# Q3 append column with no of days difference from present date to each order date
days_diff <- function(df){
  print("Q3 append column with no of days difference from present date to each order date")
  # write code to return pandas dataframe
  df['days_diff'] <- round(now()- df$OrderDate)
  return(df)
}

# Q4 get dataframe with manager as first column and  salesman under them as lists in rows in second column.
mgr_slsmn <- function(df){
  print("Q4 get dataframe with manager as first column and salesman under them as lists in rows in second column.")
  # write code to return pandas dataframe
  mgr_slsmn <- aggregate( SaleData$SalesMan , by = list( SaleData$Manager ) , 
                          function(x) paste0((unique(x))))
  colnames(mgr_slsmn) <- c('manager','list_of_salesmen')
  return(mgr_slsmn)
}


# Q5 For all regions find number of salesman and number of units
slsmn_units <- function(df){
  # write code to return pandas dataframe
  print("Q5 For all regions find number of salesman and number of units")
  slsmn_units = df %>%
    select(Region,SalesMan,Units) %>%
    group_by(Region) %>%
    summarise(SalesMan = length(unique(SalesMan)), Units = sum(Units))
  colnames(slsmn_units) <- c('region', 'salesmen_count','total_sales')
  return(slsmn_units)
}

# Q6 Find total sales as percentage for each manager
sales_pct <- function(df){
  # write code to return pandas dataframe
  print("Q6 Find total sales as percentage for each manager")
  q10 <- df %>%
    select(Manager,Sale_amt) %>%
    group_by(Manager) %>%
    summarise(Sale_amt = sum(Sale_amt))
  q10$percent_sales <- (q10$Sale_amt / sum(q10$Sale_amt))*100
  return(q10)
}


# Q7 get imdb rating for fifth movie of dataframe
fifth_movie <- function(df){
  # write code here
  print("Q7 get imdb rating for fifth movie of dataframe")
  fifth_movie <- data.frame(subset(df, type == "video.movie", select = imdbRating))[5,]
  return(fifth_movie)
}

# Q8 return titles of movies with shortest and longest run time

movies <- function(df){
  # write code here
  print("Q8 return titles of movies with shortest and longest run time")
  movies <- data.frame(subset(df, ((df$duration == max(df$duration,na.rm = TRUE)) | (df$duration ==  min(df$duration,na.rm = TRUE))), select = title))
  return(movies)
}

# Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)
sort_df <- function(df){
  # write code here
  print("Q9 sort by two columns - release_date (earliest) and Imdb rating(highest to lowest)")
  df <- data.frame(subset(df,(((df$year > 1900) & (df$year < 2021)) & ((df$imdbRating > 0.0) & (df$imdbRating < 10.1)))))
  sort_df = df[order(df$year,df$imdbRating, decreasing = c(FALSE, TRUE)),]
  return(sort_df)
}
  
# Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes
subset_df <- function(df){
  # write code here
  print("Q10 subset revenue more than 2 million and spent less than 1 million & duration between 30 mintues to 180 minutes")
  list_col <- c('revenue','spent','duration')
  condition <- c("df$revenue > 2000000",
             "df$spent < 1000000",
             "between(df$duration,30,180)")
  print(nrow(df))
  for(i in 1:(length(list_col))){
    if(list_col[i] %in% colnames(df)){
      print(list_col[i])
      df <- data.frame(subset(df,eval(parse(text = condition[3]))))   
      print(nrow(df))
    }
  }
return(df)
}

# Q11 count the duplicate rows of diamonds DataFrame.
dupl_rows <- function(df){
  # write code here
  print("Q11 count the duplicate rows of diamonds DataFrame.")
  return(nrow(df) - nrow(data.frame(unique(df))))
}

# Q12 droping those rows where any value in a row is missing in carat and cut columns

drop_row <- function(df){
  # write code here
  print("Q12 droping those rows where any value in a row is missing in carat and cut columns")
  drop_row <- data.frame(df[(complete.cases(df[, c("carat", "cut")])),])
  return(drop_row)
}

# Q13 subset only numeric columns
sub_numeric <- function(df){
  # write code here
  print("Q13 subset only numeric columns")
  sub_numeric <- data.frame(dplyr::select_if(df, is.numeric))
  return(sub_numeric)
}

# Q14 compute volume as (x*y*z) when depth > 60 else 8

volume <- function(df){
  # write code here
  print("Q14 compute volume as (x*y*z) when depth > 60 else 8")
  df['volume'] <- apply(df[,c('x','y','z','depth')], 1, function(row) ifelse( as.numeric(row['depth']) > 60, as.numeric(row['x'])*as.numeric(row['y'])*as.numeric(row['z']), 8) )
  return(df)
}

# Q15 impute missing price values with mean
impute <- function(df){
  # write code here
  df[is.na(df[,'price']),'price'] <- colMeans(df[,'price'], na.rm = TRUE)
  return(df)
}

print("************************#####***************************")
SaleData <- read_excel("SaleData.xlsx")
View(SaleData)
print("************************")
print(least_sales(SaleData))
print("************************")
print(sales_year_region(SaleData))
print("************************")
print(days_diff(SaleData))
print("************************")
print(mgr_slsmn(SaleData))
print("************************")
print(slsmn_units(SaleData))
print("************************")
print(sales_pct(SaleData))
print("************************")
print("************************#####***************************")

imdb <- read_delim("imdb.csv", 
                   delim=',', 
                   escape_double=FALSE,
                   escape_backslash=TRUE
                   )
View(imdb)
print(fifth_movie(imdb))
print("************************")
print(movies(imdb))
print("************************")
print(head(sort_df(imdb)))
print("************************")
print(head(subset_df(imdb)))
print("************************")
print("************************#####***************************")

diamonds <- read_csv("diamonds.csv")
View(diamonds)
print(dupl_rows(diamonds))
print("************************")
print(drop_row(diamonds))
print("************************")
print(head(sub_numeric(diamonds)))
print("************************")
print(head(volume(diamonds)))
print("************************")
print(head(impute(diamonds)))
