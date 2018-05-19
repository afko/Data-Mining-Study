# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 20:28:51 2016

@author: 김성제
"""

from sklearn import datasets

x1, y1 = datasets.make_moons(n_samples=200, noise=0.1)

x2, y2 = datasets.make_circles(n_samples=200, noise=0.1, factor=0.5)

from sklearn.cluster import DBSCAN
dbscan = DBSCAN(eps=0.1, min_samples=3)
dbscan.fit(x1)

cores = dbscan.core_sample_indices_
comp = dbscan.components_

cls1 = dbscan.labels_

import numpy as np

np.unique(cls1)



iris = datasets.load_iris()

x=iris.data
y=iris.target

from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering

km = KMeans(n_clusters=3)
ac = AgglomerativeClustering(n_clusters=3)

km.fit(x)
ac.fit(x)

km_label=km.labels_
ac_label=ac.labels_

from sklearn import metrics

print(metrics.adjusted_rand_score(y,km_label))
print(metrics.adjusted_rand_score(y,ac_label))

print(metrics.homogeneity_score(y,km_label))
print(metrics.homogeneity_score(y,ac_label))

#실루엣 쓰려면 input을 써야한다.
print(metrics.silhouette_score(x,km_label))
print(metrics.silhouette_score(x,ac_label))

#ImageLoad

import matplotlib.image as im
import matplotlib.pyplot as plt
import os

## fname='sunflower.jpg'
## img = im.imread(os.path.join(r'C:\Users\김성제\Desktop',fname))
sunflower = im.imread(os.path.join(r'C:\Users\김성제\Desktop\sunflower.jpg'))

R=sunflower[:,:,0]
G=sunflower[:,:,1]
B=sunflower[:,:,2]

#배열차원바꿀떄 ravel을 쓴다.
R.ravel()
G.ravel()
B.ravel()
#위에 3개랑 밑에 한줄이랑 똑같음
newx = np.c_[R.ravel(),G.ravel(),B.ravel()]

km=KMeans(n_clusters=3)
km.fit(newx)

km_label=km.labels_
km_cent = km.cluster_centers_

centx = np.zeros(newx.shape)

for i in range(3):
    centx[km_label==i,:]=km_cent[i]

newR = np.reshape(centx[:,0],R.shape)
R.shape
newG = np.reshape(centx[:,1],R.shape)
newB = np.reshape(centx[:,2],R.shape)

newim = np.zeros(sunflower.shape)
newim[:,:,0]= newR
newim[:,:,1]= newG
newim[:,:,2]= newB

plt.imshow(sunflower)
plt.imshow(newim)



