# logreg.r

# This script should do logistic regression.
# Demo:
# R -f logreg.r

# As of today, allpredictions.csv contains 8955 rows.
# 8900 - 2600 is 6300 is 6300 days is 25 years.
# I should learn from 25 years of data:
csv_l = read.csv('http://www.spy611.com/csv/allpredictions.csv')[c(2600:8900) , ]

labels = (csv_l$pctlead > median(csv_l$pctlead))

# Now I should learn:
mymodel = glm(labels ~ pctlag1 + pctlag2 + pctlag4 + pctlag8 + pctlag16, data=csv_l, family='binomial')
mymodel

# The above model assumes that each label relies somewhat on pctlag1,2,4,8,16
# The model returns the probability that label is TRUE
# If the probability is above 0.51 I consider that a bullish prediction.
# If the probability is below 0.49 I consider that a bearish prediction.

# Now I should predict one observation (quiet day):
just1x = list(pctlag1=0.001,pctlag2=0.001,pctlag4=0.001,pctlag8=0.001,pctlag16=0.001)
updown_prediction = predict(mymodel,just1x, type='response')
updown_prediction

# Now I should predict one observation (strong down day):
just1x = list(pctlag1=-2.1,pctlag2=-2.2,pctlag4=-2.4,pctlag8=-2.8,pctlag16=-2.16)
updown_prediction = predict(mymodel,just1x, type='response')
updown_prediction

# Now I should predict one observation (strong up day):
just1x = list(pctlag1=2.1,pctlag2=2.2,pctlag4=2.4,pctlag8=2.8,pctlag16=2.16)
updown_prediction = predict(mymodel,just1x, type='response')
updown_prediction
