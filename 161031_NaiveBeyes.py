# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from sklearn import datasets
import numpy as np
import pandas as pd

iris = datasets.load_iris()
x = iris.data
y = iris.target

#Binary로 바꾸기
x_mean = np.mean(x,axis=0)
x[0]>x_mean
(x>x_mean)*1

x_new = (x>x_mean)*1

from sklearn.naive_bayes import BernoulliNB

bernNB = BernoulliNB()
bernNB.fit(x_new, y)

bernNB.class_log_prior_
np.exp(bernNB.class_log_prior_)

bernNB.feature_log_prob_
np.exp(bernNB.feature_log_prob_)

x_min=np.min(x,axis=0)
x_max=np.max(x,axis=0)

x_minmean = (x_min + x_mean)/2
x_maxmean = (x_max + x_mean)/2

x_new=np.zeros(shape=(150,4),dtype='int')
for i in range(150):
    for j in range(4):
        if x[i,j]<=x_minmean[j]:
            x_new[i,j]=1
        elif x[i,j]<=x_mean[j]:
            x_new[i,j]=2
        elif x[i,j]<=x_maxmean[j]:
            x_new[i,j]=3
        else:
            x_new[i,j]=4
            
from sklearn.naive_bayes import MultinomialNB

multiNB = MultinomialNB()
multiNB.fit(x_new,y)
multiNB.predict(x_new)
multiNB.predict_proba(x_new)

np.exp(multiNB.feature_log_prob_)
np.sum(np.exp(multiNB.feature_log_prob_), axis=1)

from sklearn.naive_bayes import GaussianNB    
gaussNB = GaussianNB()
gaussNB.fit(x,y)
gaussNB.theta_        
gaussNB.sigma_