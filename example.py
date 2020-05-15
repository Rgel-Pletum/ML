import numpy as np
import pandas as pd



data = pd.read_csv('titanic.csv', index_col='PassengerId')





f=data['Sex']
b=data['Name']
b=data['Sex'].value_counts()
print(b)
res = data['Name'].get_values()
list_name = []
for row in res:
	if ("Miss." in row):
		i=row.find(".")
		trname=row[i+2:]
		i=trname.find(" ")
		trname=trname[:i]
		list_name.append(trname)
	if ("Mrs." in row):
		i = row.find("(")
		trname = row[i + 1:]
		i = trname.find(" ")
		trname = trname[:i]
		list_name.append(trname)
print(list_name)
dd = {'Name':list_name}
df = pd.DataFrame(dd)
print(df)
b=df['Name'].value_counts()
print(b)	







