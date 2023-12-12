import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

df =pd.read_csv("Iris.csv")

df =df.drop(['Id'],axis=1)
print(df.columns)

#outliers 
#missing values 
#balance of the data 
#if the data is normal 

x = df.drop(["Species"],axis=1)
y = df.Species

X_train,X_test,Y_train,Y_test = train_test_split(x,y,test_size =0.2,stratify=y)

tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train,Y_train)

# from sklearn.datasets import load_iris

# iris = load_iris()
# x = iris.data
# y = iris.target

# import matplotlib.pyplot as plt
# from sklearn.tree import plot_tree 

# plot_tree(tree,feature_names=iris.feature_names,class_names=list(iris.target_names))
# plt.show()

pred_tree = tree.predict(X_test)
print("Decision Tree acc")
print("Accuracy : ",accuracy_score(Y_test,pred_tree ))

forest = RandomForestClassifier(n_estimators=100,random_state=42)
forest.fit(X_train,Y_train)

pred_forest = forest.predict(X_test)
print("forest acc")
print("Accuracy : ",accuracy_score(Y_test,pred_forest ))