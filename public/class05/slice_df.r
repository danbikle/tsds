# slice_df.r

# This script should slice rows and columns of a Data Frame.

# Demo:
# R -f slice_df.r

# First I should get a list:
csv_l  = read.csv('http://www.spy611.com/csv/allpredictions.csv')

# I should convert my list into a Data Frame:
csv_df = data.frame(csv_l)

# I should get rows 20 through 30:
rows2030 = csv_df[c(20:30) , ]
rows2030

# I should get columns 1 through 8:
cols18 = csv_df[, c(1:8)]
head(cols18)

# I should get rows 20 through 30 and columns 1, 2, 4, 6, 8:
rows2030_12468 = csv_df[c(20:30) , c(1,2,4,6,8)]
rows2030_12468
