import pandasql as psql 

meat=psql.load_meat()
print(meat.head())

sdfc=psql.sqldf('select pork, veal, beef from meat')
print(sdfc.head())

a=psql.sqldf('select * from meat where beef>700')
print(a)

