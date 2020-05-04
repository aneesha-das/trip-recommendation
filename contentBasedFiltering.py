# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:32:33 2020

@author: Aneesha
"""


from utils.contentBasedFilterUtils import getTopRecommendations

title='Manali'
methods=['cosine','euclidean', 'manhattan']
for m in methods:
    places=getTopRecommendations(title,method=m)
    print("Since you have liked "+title+", you may like (By "+m+" method):")
    for x in places:
        print(x)


