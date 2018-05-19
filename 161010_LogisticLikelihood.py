# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 15:40:07 2016

@author: 김성제
"""
import math

def sum_function(a,b):
    return a+b 
#    두 줄을 동시에 run해야함
    
    print(sum_function(3,5))

    
# 그냥 binary    
def likelihood_binary(x,p):
    return p**x*(1-p)**(1-x)
    
    likelihood =1
    p=0.2
    D=[1,0,1,1,1,0,1,0]
    for x in D:
        #likelihood = likelihood*likelihood_binary(x,p)
        likelihood*= likelihood_binary(x,p)
   
        
        print(likelihood)

#logistic_likelihood
def logistic_likelihood(x,y,b0,b1):
    p = 1/(1+math.exp(-b0-b1*x))
    return p**y*(1-p)**(1-y)
    
    likelihood1 = 1
    b0=-2
    b1=0.1
        
    D1=[[30,1],[22,0],[15,0],[26,1],[17,0],[20,0]]
    
    for x,y in D1:
        likelihood1*= logistic_likelihood(x,y,b0,b1)
        
        print(likelihood1)

import pandas as pd

        
        