# df1.r

# ref:
# http://www.dummies.com/how-to/content/how-to-create-a-data-frame-from-scratch-in-r.html

employee <- c('John Doe','Peter Gynn','Jolie Hope')
salary <- c(21000, 23400, 26800)
startdate <- as.Date(c('2010-11-1','2008-3-25','2007-3-14'))

employ.data = data.frame(employee, salary, startdate)

typeof(employ.data)
# I should see: "list"
