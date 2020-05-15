import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data0 = pd.read_csv('titanic.csv', index_col='PassengerId')

data=data0.dropna(how='any', subset=['Fare', 'Age','Pclass','Sex','Survived'], axis=0)


Fare = data['Fare'].get_values()
Age = data['Age'].get_values()
Pclass = data['Pclass'].get_values()
Sex0 = data['Sex'].get_values()
Survived = data['Survived'].get_values()
Sex=[]
for gen in Sex0:
	if (gen=='female'):
		Sex.append(0)
	else:
		Sex.append(1)
print(type(Fare))
#print(Fare)
print(Fare.shape)
Fare = Fare.transpose()
#print(Fare)
print(Fare.shape)
	
Proper=np.vstack((Fare, Age))
Proper=np.vstack((Proper, Pclass))
Proper=np.vstack((Proper, Sex))
print(Proper.shape)
Proper=Proper.transpose()
print(Proper.shape)
#print(Proper)
x = np.array(Proper)
y = np.array(Survived)
clf = DecisionTreeClassifier(random_state=241)
clf.fit(x, y)
importances = clf.feature_importances_
print(importances)
print(clf.predict([[10, 20, 2, 1]]))