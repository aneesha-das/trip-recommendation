# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:47:36 2020

@author: Aneesha
"""
from utils.formatDataForContentBasedAnalysis import getPlaces
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

data=getPlaces()
place_dict={}
matrix=data.to_numpy()
rows=matrix.shape[0]
for i in range(0,rows,1):
    place_dict[data.index[i]]=matrix[i][1]

def getTopRecommendations(title,method,column='tags',count=10):
    if(method=='cosine'):
        similarity=getCosineSimilarity(column);
    title_index=data[data['name']==title].index[0]
    sorted_index=pd.Series(similarity[title_index]).sort_values(ascending=False)
    top_index=list(sorted_index.iloc[0:count+1].index)
    place_names=[]
    for place in top_index:
        if(place!=title_index):
            place_names.append(place_dict[place])
    return place_names

            
def getCosineSimilarity(column):
    count = CountVectorizer()
    vector = count.fit_transform(data[column])
    cosine_sim = cosine_similarity(vector, vector)
    return cosine_sim
