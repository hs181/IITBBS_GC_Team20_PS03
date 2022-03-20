
# WATER QUALITY PREDICTION

The purpose of this project is to deliver a machine learning solution to predict the quality of the water for the given sample parameters.This repository contains the code to predict water quality by using various machine learning models. 

# TABLE OF CONTENTS
i) Getting Started

ii) Data Preprocessing 

iii) Data Visualisation

iv) Observing the effect of Outliers

iv)Training with different ML algorithms

v) Training with Deep Learning algorithm

vi) Computing the F1 SCORES

vii) Creating a web app using ANVIL app designer

viii) Contacts of contributors

# Getting Started

The training dataset was uploaded in the google drive in the following link:
<p> https://drive.google.com/file/d/1HBbbwZ5cCj_Xp6yR8MTkTgDuSOVo9dj5/view
  
This dataset path was imported into the "GOOGLE COLAB" which is an online based compiler for ML algorithms, which has most of the libraries preinstalled. All the necessary libraries like 'numpy', 'pandas', and 'matplotlib' were imported so that we can use them on our dataset.

# Data Preprocessing 

First we have imported the dataset in the pandas frame using the pandas library that we imported before, and created the matrix of features and the dependent variable vector and we have also observed that there were minority classes in the dataset which might be ignored by our model during prediction. Hence we have applied SMOTE (synthetic minority oversampling technique) to increase the number of minority samples in our data so that our ML model won't ignore them during training part. Further information can be read in the following link
  
<p> https://towardsdatascience.com/smote-fdce2f605729
  

We have also applied the info() method to chech whether there were any missing values in the data and found no missing values and since all the training data was having numerical datatype, we don't need to encode any data as well. 

# Data Visualisation
  
 For visualisation purpose, we have used heatmaps and boxplots to observe the correlation and the outliers in our data respectively. Following are the images we obtained:

  ## HEATMAP WITHOUT SMOTE
![alt text](https://github.com/hs181/IITBBS_GC_Team20_PS03/blob/main/Corrleation_plots/CORR_WITHOUT_SMOTE.png)
  ## HEATMAP WITH SMOTE
![alt text](https://github.com/hs181/IITBBS_GC_Team20_PS03/blob/main/Corrleation_plots/CORR_WITH_SMOTE.png)
  
  ## BOXPLOT FOR SOME PARAMETERS
  
 ![alt text](https://github.com/hs181/IITBBS_GC_Team20_PS03/blob/main/Box-plots-visualisation/Mud.png)
 ![alt text](https://github.com/hs181/IITBBS_GC_Team20_PS03/blob/main/Box-plots-visualisation/P15.png)
  
  
 # OBSERVING THE EFFECT OF OUTLIERS
 
  ![image](https://user-images.githubusercontent.com/84396869/159155069-7fd184fb-358d-414e-91e6-5fc5734920f8.png)

  We have tried to remove the outliers so as to simplify our future ML models but when we observed the box plots we see that outliers mostly consist of the minority class and removing them will mean removing the minority class data which might affect our accuracy of our ML model hence we have decided to not do so.
  
  # TRAINING WITH DIFFERENT MACHINE LEARNING ALGORITHMS
  
We have first used logistic regression as it is a basic algorithm for binary classification without using SMOTE and with using SMOTE and observed that we were getting better results with SMOTE and then we have decided to continue to use SMOTE for the rest of the algorithms
Following are the classification algorithms we used to train our model on the given dataset:
  1)Decision Tree classifier
  2)Light GBM
  3)Logistic Regression
  4) Naive Bayes
  5) Random Classifier with 50 decision trees 
  6) Random Classifier with 100 decision trees 
  7) Random Classifier with 150 decision trees 
  8) Support Vector Machine with radial basis function as our kernel
  9) XG BOOST
  
 # TRAINING WITH DEEP LEARNING ALGORITHM (ARITFICIAL NEURAL NETWORK)
  
  We have also used the deep learning algorithm since they are mostly known for their powerful computation. We have initially created a shallow learning network which was producing results close to 95 %. Then we tried using the deep learning network also known as ANN which is mainly used in classification and regression
  We choose the following parameters while training with ANN:
   i) batch_size=32
  ii) epochs=20( The accuracy was converging after the 11th epoch)
  iii)loss='binary_crossentropy' (This is specifically used for binary classification')
  iv) optimizer='adam' (The most useful one)
 
 # COMPUTING THE F1 SCORES
  
  |MODEL|F1 SCORE IN PERCENT|
  |-----|-------------------|
  |LOGISTIC REGRESSION WITHOUT SMOTE|85.5|
  |LOGISTIC REGRESSION WITH SMOTE|96.153|
  |DECISION TREE CLASSIFIER|99.83|
  |LIGHT GBM|99.9252|
  |NAIVE BAYES|91.287|
  |RANDOM FOREST CLASSIFIER WITH 50 DECISION TREES|99.9807|
  |RANDOM FOREST CLASSIFIER WITH 100 DECISION TREE|99.98604|
  |RANDOM FOREST CLASSIFIER WITH 150 DECISION TREE|99.98677|
  |SVM (KERNEL=RBF)|99.21|
  |XG BOOST|99.97|
  
  # CREATING THE WEB APP USING ANVIL APP DESIGNER
  
  Anvil is one of the most sophisticated website to create web apps exclusively in python. The main reason for us to use this anvil is because it enables an uplink to which we can connect to google colab and run it at our web app backend. 
  You can check out the app link here :
  <p> https://water-quality-prediction-team20.anvil.app
    
 # CONTACTS OF CONTRIBUTORS
    
Harshit Saini ---- <hs18@iitbbs.ac.in>
    
Vamsi Bharadwaj ---- <cvb15@iitbbs.ac.in>
    
Raghu Vamsidhar ---- <srv12@iitbbs.ac.in>
    
K. Harish ---------- <kh16@iitbbs.ac.in>
  
