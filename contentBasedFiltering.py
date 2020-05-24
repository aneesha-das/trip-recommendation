# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:32:33 2020

@author: Aneesha
"""


from utils.contentBasedFilterUtils import getTopRecommendations

#'cosine','euclidean','pearson','spearman','kendall','jaccard','knn'
title='Haridwar'
methods=['cosine','pearson','knn']
for m in methods:
    places=getTopRecommendations(title,method=m, weighted=False)
    # print()
    # print("Since you have liked "+title+", you may like (By "+m+" method) without Weights:")
    # for x in places:
    #     print(x+ " coefficient: %.2f"%places[x])
    # if m!='jaccard':
    places=getTopRecommendations(title,method=m, weighted=True)
    print()
    print("Since you have liked "+title+", you may like (By "+m+" method) with Weights:")
    for x in places:
        print(x+ " coefficient: %.2f"%places[x])