import pandas as pd #for reading dataset
import numpy as np 
import sklearn.metrics
from sklearn.metrics import accuracy_score


dataset = pd.read_csv("heart.csv")#reading dataset
##print(dataset) # printing dataset

x = dataset.iloc[:,:-1].values #locating inputs
y = dataset.iloc[:,-1].values #locating outputs

#printing X and Y
print("x=",x)
print("y=",y)

from sklearn.model_selection import train_test_split # for splitting dataset
x_train,x_test,y_train,y_test = train_test_split(x ,y, test_size = 0.25 ,random_state = 0)
#printing the spliited dataset
print("x_train=",x_train)
print("x_test=",x_test)
print("y_train=",y_train)
print("y_test=",y_test)
 #importing algorithm
from sklearn.tree import DecisionTreeClassifier
classifier=DecisionTreeClassifier()
classifier.fit(x_train,y_train)#trainig Algorithm

y_pred=classifier.predict(x_test) #testing model
print("y_pred",y_pred) # predicted output
print("ACCURACY SCORE  = ",accuracy_score(y_test, classifier.predict(x_test)))

from sklearn.metrics import classification_report
print(classification_report(y_test,y_pred))

a1=int(input("age= "))
b1=int(input("sex= "))
c1=int(input("cp= "))
d1=int(input("trestbps= "))
e1=int(input("chol= "))
f1=int(input("fbs= "))
g1=int(input("restecg= "))
h1=int(input("thalach= "))
i1=int(input("exang= "))
j1=float(input("oldpeak= "))
k1=int(input("slope= "))
l1=int(input("ca= "))
m1=int(input("thal= "))
















##
a = classifier.predict([[a1,b1,c1,d1,e1,f1,g1,h1,i1,j1,k1,l1,m1]])
print('Predicted Output: %s' % int(a))


