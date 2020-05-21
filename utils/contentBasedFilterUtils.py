# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:47:36 2020

@author: Aneesha
"""
from utils.formatDataForContentBasedAnalysis import getPlaces
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import jaccard_score
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import manhattan_distances
from scipy.stats import pearsonr
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import numpy as np
from scipy import sparse

data=getPlaces()
place_dict={}
matrix=data.to_numpy()
rows=matrix.shape[0]
for i in range(0,rows,1):
    place_dict[data.index[i]]=matrix[i][1]

def getTopRecommendations(title,method,count=10,weighted=True):
    if method=='jaccard' or not weighted:
        countVector = CountVectorizer()
        vector = countVector.fit_transform(data['tags'])
    else:
        vector=sparse.csr_matrix(data['weight'].to_list())
    ascending_order=False;
    if method=='cosine':
        similarity=getCosineSimilarity(vector)
    elif method=='euclidean':
        similarity=getEuclideanSimilarity(vector)
        ascending_order=True
    elif method=='manhattan':
        ascending_order=True
        similarity=getManhattanSimilarity(vector)
    elif method=='knn':
        return getKNNSimilarity(vector,title)
    else:
        return getPairwiseSimilarity(vector,title,method,count)
    title_index=data[data['name']==title].index[0]
    sorted_index=pd.Series(similarity[title_index]).sort_values(ascending=ascending_order)
    top_index=list(sorted_index.iloc[0:count+1].index)
    top_values=list(sorted_index.iloc[0:count+1])
    place_names={}
    i=0;
    for place in top_index:
        if place!=title_index:
            place_names[place_dict[place]]=top_values[i]
        i+=1
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

def getPairwiseSimilarity(vector,title,method,count):
    tag_vector=np.array(vector.todense()) 
    title_index=data[data['name']==title].index[0]
    coeffs=[]
    if method=='pearson':
        for i in tag_vector:
            coeff,p_value=pearsonr(tag_vector[title_index], i)
            coeffs.append(coeff)
    elif method=='spearman':
        for i in tag_vector:
            coeff,p_value=spearmanr(tag_vector[title_index], i)
            coeffs.append(coeff)
    elif method=='kendall':
        for i in tag_vector:
            coeff,p_value=kendalltau(tag_vector[title_index], i)
            coeffs.append(coeff)
    elif method=='jaccard':
        for i in tag_vector:
            coeffs.append(jaccard_score(tag_vector[title_index], i))
    sorted_index=pd.Series(coeffs).sort_values(ascending=False)
    top_index=list(sorted_index.iloc[0:count+1].index)
    top_values=list(sorted_index.iloc[0:count+1])
    place_names={};
    i=0;
    for place in top_index:
        if(place!=title_index):
            place_names[place_dict[place]]=top_values[i]
        i+=1
    return place_names
        
def getKNNSimilarity(vector,title):
    tag_vector=np.array(vector.todense()) 
    title_index=data[data['name']==title].index[0]
    liked_place=tag_vector[title_index]
    nbrs=NearestNeighbors(n_neighbors=11).fit(tag_vector)
    nearest_matches=nbrs.kneighbors([liked_place])
    place_names={}
    i=0
    for place in nearest_matches[1][0]:
        if place!=title_index:
            place_names[place_dict[place]]=nearest_matches[0][0][i]
        i+=1
    return place_names

def getWeights():
    vector=sparse.csr_matrix(data['weight'].to_list())
    return vector
    
    