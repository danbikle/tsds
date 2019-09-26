# ts1.r

# This script should plot a time series.

# Demo:
# R --no-save
# then:
# source('ts1.r')

# I need only three lines of syntax:

csv_l = read.csv('http://www.spy611.com/csv/allpredictions.csv')[ , c('cdate','cp')]
my_d  = as.Date(csv_l$cdate, "%Y-%m-%d")
plot(csv_l$cp ~ my_d)





