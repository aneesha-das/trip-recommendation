# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:17:26 2020

@author: Amit
"""


import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

def getCollabFilteringRecommendations(place_name):
    rating_data=pd.read_csv('temp_ratings.csv')
    place_data=pd.read_csv('temp_places.csv')
    #mean_ratings=rating_data.groupby('place_id')['rating'].mean()
    combined_place_data=pd.merge(place_data,rating_data,left_on="id",right_on="place_id")
    #place_data=place_data.merge(mean_ratings, left_on="id", right_on="place_id")
    rating_tabular_data=combined_place_data.pivot_table(values='rating',index='user_id',columns='name',fill_value=0)
    transpose=rating_tabular_data.values.T
    SVD=TruncatedSVD(n_components=12,random_state=17)
    resultant_matrix=SVD.fit_transform(transpose)
    correlation_data=np.corrcoef(resultant_matrix)
    place_names=rating_tabular_data.columns
    place_list=list(place_names)
    index=place_list.index(place_name)
    corr_column=correlation_data[index]
    return corr_column
    #return list(place_names[(corr_column<1.0) & (corr_column>0.6)])

def getUserWiseCollabFilteringRecommendations(user_id):
    rating_data=pd.read_csv('temp_ratings.csv')
    user_ratings=rating_data[rating_data["user_id"]==user_id]
    interested_places=user_ratings[user_ratings["rating"]>5]
    place_data=pd.read_csv('temp_places.csv')
    places=place_data.copy(True)
    place_data=place_data.merge(interested_places, left_on="id", right_on="place_id")
    corr_result=[]
    for index in place_data.index:
        corr_column=getCollabFilteringRecommendations(place_data['name'][index])
        rating=place_data['rating'][index]
        corr_column=corr_column* rating
        if len(corr_result)==0:
            corr_result=corr_column
        else:
            corr_result=np.add(corr_result,corr_column)
    if len(corr_result)>0:
        corr_result=corr_result/(len(place_data)*10)
        place_names=places["name"]
        print(place_names[(corr_column<1.0) & (corr_column>0.5)])
        return
    print("Insufficient data")
    