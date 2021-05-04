import datetime as dt
format = '%Y-%m-%dT%M:%s'
t1 = dt.datetime.strptime('2008-10-12T14:45:52',format)
print('Day' + str(t1.day))
print('Month'+ str(t1.minute))
print('minute'+ str(t1.second))

t2 = dt.datetime.now()
diff = t2-t1
print('how many days difference'+ str(diff.days))
