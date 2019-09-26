# dataframe.r

# This script shows how to build a Data Frame from a CSV file.
# Demo:
# R -f dataframe.r

# First I should get a list:
csv_l  = read.csv('http://www.spy611.com/csv/allpredictions.csv')

# I should convert my list into a Data Frame:
csv_df = data.frame(csv_l)

# I should visualize the Data Frame:
typeof(csv_df)
head(csv_df)
summary(csv_df)
