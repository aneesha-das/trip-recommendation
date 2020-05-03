# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:32:33 2020

@author: Aneesha
"""


from utils.contentBasedFilterUtils import getTopRecommendations

title='Manali'
places=getTopRecommendations(title,method='cosine')
print("Since you have liked "+title+", you may like:")
for x in places:
    print(x)


