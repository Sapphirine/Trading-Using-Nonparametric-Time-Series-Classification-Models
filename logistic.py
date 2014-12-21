
# coding: utf-8

# In[1]:

from numpy import genfromtxt
import numpy as np
import datetime as datatime
my_data = genfromtxt("C:\\Users\\Yufan\\Google Drive\\Interviews\\Interviews Github\\BitCoinTotalReturnSwapStrategy\\bitfinexUSD.csv\\.bitfinexUSD.csv", delimiter =',')




# In[2]:

print my_data.shape
my_data_cut = my_data
        
        


# In[3]:

import sklearn.linear_model as linear


# In[7]:

L = my_data.shape[0]
n_training_sample_size = int(L*.9) - 11
print n_training_sample_size

n_testing_sample_size = L - n_training_sample_size -11
n_testing_sample_size 



# In[12]:

N = n_training_sample_size
training_data = np.zeros((N,11))
print training_data.shape
for i in xrange(N):
    for j in xrange(10):
        training_data[i,j] = my_data_cut[i-j+10,1]/my_data_cut[i-j+9,1] #from index 11 
    
    if (my_data_cut[i+11,1] > my_data_cut[i+10, 1]):
        training_data[i,10] = 1
  
N = n_testing_sample_size
testing_target = np.zeros((N,1))-1
testing_data = np.zeros((N,10))
reset = n_training_sample_size
print reset
for i in xrange(N):
    for j in xrange(10):
        testing_data[i,j] = my_data_cut[reset+i-j+10,1]/my_data_cut[reset+i-j+9,1]
    if (my_data_cut[i+reset+11,1] > my_data_cut[i+reset+10, 1]):
        testing_target[i,0] = 1
    else:
        testing_target[i,0] = 0
        


# In[9]:

logistic_regression_model = linear.LogisticRegression()
training_data.shape


# In[10]:

logistic_regression_model.fit(training_data[:,0:-1],training_data[:,10:11])


# In[16]:

beta = logistic_regression_model.coef_
beta_0 = logistic_regression_model.intercept_

predicted_value = logistic_regression_model.predict_proba(testing_data)
hit = 0
for i in xrange(len(predicted_value)):
    if predicted_value[i,1] > 0.5 and testing_target[i,0] == 1 or predicted_value[i,1] < 0.5 and testing_target[i,0] == 0:
        hit +=1 

print hit

print len(predicted_value)
print len(testing_target)

print beta
print beta_

print predicted_value


# In[15]:

nd = my_data_cut
print nd


# In[17]:

predicted_v = logistic_regression_model.score(testing_data,testing_target)


# In[18]:

predicted_v

