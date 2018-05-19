# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 15:25:02 2016

@author: 김성제
"""

import numpy as np

f = open(r'C:\Users\김성제\Desktop\transaction.txt','r')

f.readline().strip().split(',')
f.close()

data=[]
for l in f:
    data.append(l.strip().split(','))
    
r1=[['b,c'],['g']]

def cal_support(r,trans):
    t_num=len(data)
    count=0
    for t in trans:
        if all([item in t for item in r]):
            count +=1
    return count/t_num
    
cal_support(r1, data)


def cal_support(r,trans):
    item_set=r[0]+r[1]
    n=len(trans)
    nitem_rule=len(item_set)
    count=0
    for t in trans:
        if sum([x in item_set for x in t ])==nitem_rule:
            count=1
        return count/n
    
def cal_confidence(r,trans):
    item_set=r[0]+r[1]
    n = len(trans)
    nitem_rule = len(item_set)
    nitem_cond = len(r[0])
    count1 =0
    count2 =0
    
    for t in trans: 
        if sum([x in r [0] for x in t])==nitem_cond:
            count1+=1
            if sum([x in item_set for x in t]) == nitem_rule:
                count2+=1
    return count2/count1

cal_support(r1,data)
cal_confidence(r1,data)

cal_support(['a','b'],data)
mis = 0.4

from functools import reduce
l=[]
for t in data:
    l+=t 
item=list(set(1))
C1=[[x]for x in items]
L1=[ x for x in C1 if cal_support(x,data)>=mins]


import itertools

C2 = [y[0]+y[1] for y in [x for x in itertools.combinations(L1, 2)]]
L2 = [x for x in C2 if cal_support(x,data)>=mins]

C3=[list(set(y[0]+y[1])) for y in [x for x in inrtertools.combiations
  if len(set(y[0]+y[1]))==3]

L3 = [ x for x in C3 if cal_support(x,data)> =mins]

L3[0]

r2=[['c','e']],['f']]

from apyori import adrioid
liest()









    
    
    