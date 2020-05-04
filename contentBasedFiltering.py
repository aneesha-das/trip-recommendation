# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:32:33 2020

@author: Aneesha
"""


from utils.contentBasedFilterUtils import getTopRecommendations

title='Digha'
methods=['cosine','euclidean','pearson','spearman','kendall','jaccard','knn']
for m in methods:
    places=getTopRecommendations(title,method=m)
    print()
    print("Since you have liked "+title+", you may like (By "+m+" method):")
    for x in places:
        print(x+ " coefficient: %.2f"%places[x])
