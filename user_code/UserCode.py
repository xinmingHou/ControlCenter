#!/usr/bin/env python
# coding: utf-8

# # This is UserCode
# 
# 在下面输入代码。

# In[ ]:


# DBSCAN


'''

Created on 2019.3.28



@author: CCNT

'''



import pandas as pd

import numpy as np



trainset = pd.read_csv('/data/algo50+/train.csv')

X = trainset.iloc[:,:].values



from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = "NaN", strategy = "mean", axis = 0)

imputer = imputer.fit(X[ : , :])

X[ : , :] = imputer.transform(X[ : , :])



from sklearn.cluster import DBSCAN

model = DBSCAN(affinity='euclidean')

model = model.fit(X)



testset = pd.read_csv('/data/algo50+/test.csv')

Y_test =  model.predict(testset)

testset['result']= Y_test

print(type(testset))

print(testset)

testset.to_csv('/data/algo50+/result.csv')



