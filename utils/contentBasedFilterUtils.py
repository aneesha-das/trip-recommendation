# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:47:36 2020

@author: Aneesha
"""
from utils.formatDataForContentBasedAnalysis import getPlaces
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd

data=getPlaces()
place_dict={}
matrix=data.to_numpy()
rows=matrix.shape[0]
for i in range(0,rows,1):
    place_dict[data.index[i]]=matrix[i][1]

def getTopRecommendations(title,method,column='tags',count=10):
    countVector = CountVectorizer()
    vector = countVector.fit_transform(data[column])
    ascending_order=False;
    if(method=='cosine'):
        similarity=getCosineSimilarity(vector)
    elif method=='euclidean':
        similarity=getEuclideanSimilarity(vector)
        ascending_order=True
    elif method=='manhattan':
        ascending_order=True
        similarity=getManhattanSimilarity(vector)
    title_index=data[data['name']==title].index[0]
    sorted_index=pd.Series(similarity[title_index]).sort_values(ascending=ascending_order)
    top_index=list(sorted_index.iloc[0:count+1].index)
    place_names=[]
    for place in top_index:
        if(place!=title_index):
            place_names.append(place_dict[place])
    return place_names

            
def getCosineSimilarity(vector):
    cosine_sim = cosine_similarity(vector, vector)
    return cosine_sim

def getEuclideanSimilarity(vector):
    eucilidean_sim = euclidean_distances(vector, vector)
    return eucilidean_sim

def getManhattanSimilarity(vector):
    manhattan_sim = manhattan_distances(vector, vector)
    return manhattan_sim
