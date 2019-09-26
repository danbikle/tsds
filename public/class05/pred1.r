# pred1.r

# This script should create and use predicates.

# Demo:
# R -f pred1.r

# First I should get a list:
csv_l  = read.csv('http://www.spy611.com/csv/allpredictions.csv')

# I should convert my list into a Data Frame:
csv_df = data.frame(csv_l)

# I should create a predicate to get all rows where cp > 2100.0:
# pred1 = (csv_df[ , c(2)] > 2100.0)
# better syntax, more concise:
pred1 = (csv_df$cp > 2100.0) 
tail(pred1)

# I should apply the predicate:
constrained_df = csv_df[pred1, ]
head(constrained_df)
tail(constrained_df)
# Above expressions should show only rows where cp > 2100.0
# Number of rows where cp > 2100.0:
nrow(constrained_df)

# I should create another predicate:
# This idea works in Python Pandas but not here:
# pred2 = (csv_df[ , c(1)] > '2016')
my_d    = as.Date(csv_df$cdate, "%Y-%m-%d")
pred3   = (my_d > '2016-01-01')

# I should show how to AND two predicates together:
pred4 = pred1 & pred3

# I should apply the predicate:
above2100in2016_df = csv_df[pred4, ]

# I should visualize the result:
above2100in2016_df[ , c('cdate','cp')]


# I should do simple predictive analytics using predicates.

# I start with a simple English question:
# If sp500 is quiet, is that bullish?

# Next, I define 'quiet':
# quiet means that -0.2 < pctlag1 < 0.2

# Then I build a predicate:
qpred1 = (-0.2 < csv_df$pctlag1)
qpred2 = (csv_df$pctlag1 < 0.2 )
qpred3 = qpred1 & qpred2

# Next, I apply the predicate:
quiet_df       = csv_df[qpred3, ]
dayafter_quiet = quiet_df$pctlead

# Then I report the results:
mean(dayafter_quiet)
median(dayafter_quiet)
mean(csv_df$pctlead)
median(csv_df$pctlead)

mean(dayafter_quiet)   > mean(csv_df$pctlead)
median(dayafter_quiet) > median(csv_df$pctlead)

# I interpret the above results by saying:
# The day after a quiet day is not bullish.

# I start with another English question:
# If sp500 is down, is that bullish?

# Next, I define 'down':
# down means that -4.0 < pctlag1 < -1.0

# Then I build a predicate:
downpred1 = (-4.0 < csv_df$pctlag1)
downpred2 = (csv_df$pctlag1 < -1.0)
downpred3 = downpred1 & downpred2

# Next, I apply the predicate:
down_df       = csv_df[downpred3, ]
dayafter_down = down_df$pctlead

# Then I report the results:
mean(dayafter_down)
median(dayafter_down)
mean(csv_df$pctlead)
median(csv_df$pctlead)

mean(dayafter_down)   > mean(csv_df$pctlead)
median(dayafter_down) > median(csv_df$pctlead)

# I interpret the above results by saying:
# The day after a down day is bullish.

# I start with another English question:
# If sp500 is up, is that bullish?

# Next, I define 'up':
# up means that 1.0 < pctlag1 < 4.0

# Then I build a predicate:
uppred1 = (1.0 < csv_df$pctlag1)
uppred2 = (csv_df$pctlag1 < 4.0)
uppred3 = uppred1 & uppred2

# Next, I apply the predicate:
up_df       = csv_df[uppred3, ]
dayafter_up = up_df$pctlead

# Then I report the results:
mean(dayafter_up)
median(dayafter_up)
mean(csv_df$pctlead)
median(csv_df$pctlead)

mean(dayafter_up)   > mean(csv_df$pctlead)
median(dayafter_up) > median(csv_df$pctlead)

# I interpret the above results by saying:
# The day after an up day is unpredictable.
