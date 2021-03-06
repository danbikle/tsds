# moy_hist.r

# This script should sum pctlead and groupby month of year
# This script should sum pctlead and groupby day   of week
# Demo:
# R -f moy_hist.r
# or
# source('moy_hist.r')

csv_l  = read.csv('http://www.spy611.com/csv/allpredictions.csv')
summary(csv_l)

# I should convert my list into a Data Frame:
csv1_df = data.frame(csv_l)

# I should sort it by cdate ascending:
csv2_df = csv1_df[order(csv1_df$cdate),]

# For 30 years, I should get cdate and cp:
len0_i  = length(csv2_df$cp)
start_i = (len0_i - 252*30)
csv3_df = csv2_df[c(start_i:len0_i), c("cdate","cp")]

# I should shift the cp column to lead me towards pctlead.
# Pandas has shift.
# In R I need to work for it:
len1_i        = length(csv3_df$cp)
lastp_f       = csv3_df$cp[len1_i]
lead0_v       = c(csv3_df$cp, c(lastp_f)) # concatenation demo
lead_v        = lead0_v[2:(len1_i+1)]
csv3_df$leadp = lead_v

# I should calculate pctlead:
csv3_df$pctlead = 100.0*(csv3_df$leadp - csv3_df$cp)/csv3_df$cp

# I should create two date-features:
csv3_df$moy = format(as.Date(csv3_df$cdate),"%m")
csv3_df$dow = format(as.Date(csv3_df$cdate),"%w")

# Report:
head(csv3_df)
tail(csv3_df)

# I should use aggregate() to sum(pctlead) groupby Month-of-Year:
agg_moy = aggregate(pctlead ~ moy, csv3_df, sum)
print('Sum of pctlead groupby Month-of-Year:')
print(agg_moy)

# I should use aggregate() to sum(pctlead) groupby Day-of-Week:
agg_dow = aggregate(pctlead ~ dow, csv3_df, sum)
print('Sum of pctlead groupby Day-of-Week:')
print(agg_dow)

# I should create a plot window of 2 rows and one col:
par(mfrow = c(2,1))

plot(agg_moy$pctlead ~ agg_moy$moy, type="h", col="blue", lwd=10)
grid()

plot(agg_dow$pctlead ~ agg_dow$dow, type="h", col="darkgreen", lwd=10)
grid()
