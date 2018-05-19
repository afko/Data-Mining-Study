# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 15:49:56 2016

@author: 김성제
"""

from sklearn.decomposition import PCA
from sklearn import datasets

iris = datasets.load_iris()
x = iris.data
y = iris.target

pca = PCA(n_components = 2)
pca.fit(x)

pca.n_components_
pca.components_

pca.explained_variance_
pca.explained_variance_ratio_

x_pca = pca.transform(x)

import matplotlib.pyplot as plt

plt.scatter(x[:,0],x[:,1],c=y,s=100)

plt.scatter(x_pca[:,0],x_pca[:,1],c=y,s=100)


from sklearn.lda import LDA

lda = LDA(n_components = 2,store_covariance=True)
lda.fit(x,y)

lda.coef_
lda.intercept_
lda.priors_
lda.means_
lda.covariance_

x_lda = lda.transform(x)

plt.scatter(x_lda[:,0],x_lda[:,1],c=y,s=100)



from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()
clf.fit(x_pca,y)
clf.score(x_pca,y)

clf.fit(x_lda,y)
clf.score(x_lda,y)
