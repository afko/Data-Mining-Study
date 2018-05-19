# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:45:02 2016

@author: 김성제
"""

#Clustrering

from sklearn import datasets
import matplotlib.pyplot as plt


x1,y1=datasets.make_moons(n_samples=200,noise=0.1)
plt.scatter(x1[:,0],x1[:,1],s=50,c=y1)

x2,y2=datasets.make_circles(n_samples=200,noise=0.1,factor=0.5)
plt.scatter(x2[:,0],x2[:,1],s=50,c=y2)

ncluster=2

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

clst1 = KMeans(n_clusters=ncluster)
clst2 = AgglomerativeClustering(n_clusters=ncluster, linkage='complete')

clst1.fit(x1)
clst2.fit(x1)

y_cls1 = clst1.labels_
y_cls2 = clst2.labels_

plt.scatter(x1[:,0],x1[:,1],s=50,c=y_cls1)
plt.scatter(x1[:,0],x1[:,1],s=50,c=y_cls2)



#Centeroid

centers = clst1.cluster_centers_
print(centers)

import numpy as np
np.mean(x1[y_cls1==0],0)
np.mean(x1[y_cls1!=0],0) 
y_cls1==0

newx1,newy1=datasets.make_circles(n_samples=20,factor=0.5,noise=0.1)
y_new1 = clst1.predict(newx1)

plt.scatter(newx1[:,0],newx1[:,1],c=y_new1,s=50)
plt.scatter(clst1.cluster_centers_[:,0],clst1.cluster_centers_[:,1],s=50,marker='d',c='k')

clst2.children_






inertia=0
centers=clst1.cluster_centers_
c=0
for c in range(ncluster):
    inertia+=np.sum(np.sqrt(np.sum((x1[y_cls1==c]-centers[c])**2,1)))
inertia

centers_agg=np.array([np.mean(x2[y_cls2==c],0) for c in range(ncluster)])
inertia_agg=0
c=0
for c in range(ncluster):
    inertia_agg+=np.sum(np.sqrt(np.sum((x1[y_cls1==c]-centers_agg[c])**2,1)))




a= np.array([[1,2],[4,6]])
b= np.array([3,5])
a-b
