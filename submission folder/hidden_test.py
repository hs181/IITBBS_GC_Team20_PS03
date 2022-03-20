#Assumption for hidden test data

#1. Data has same number of columns and in the same order as the train datset
#2. No null or undefined or missing values in the test data similar to train dataset

#importing the required libraries
import pandas as pd
import numpy as np
import pickle 



df = pd.read_csv("Hidden_test.csv")

#Dropping the parameters which are highly correlated 
# and were also dropped during training
df = df.drop(['P12','P17','P18'], axis=1)

#X = df.drop('Class',axis='columns')
#Dropping the index and time columns
X = df.iloc[:,2:-1]
Y = df['Class']

#Loading the model
with open("Random_forest_150_trees_final.pkl","rb") as f:
    classifier = pickle.load(f)

prediction = classifier.predict(X)

from sklearn.metrics import f1_score,confusion_matrix
cm=confusion_matrix(Y,prediction)
print(cm)
f1_score(Y,prediction,average='macro')





