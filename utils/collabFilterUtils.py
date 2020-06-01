# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:17:26 2020

@author: Amit
"""


import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD

def getCollabFilteringRecommendations(place_name):
    rating_data=pd.read_csv('user_place_mapping.csv')
    place_data=pd.read_csv('places.csv')
    mean_ratings=rating_data.groupby('place_id')['rating'].mean()
    combined_place_data=pd.merge(place_data,rating_data,left_on="id",right_on="place_id")
    place_data=place_data.merge(mean_ratings, left_on="id", right_on="place_id")
    rating_tabular_data=combined_place_data.pivot_table(values='rating',index='user_id',columns='name',fill_value=0)
    transpose=rating_tabular_data.values.T
    SVD=TruncatedSVD(n_components=12,random_state=17)
    resultant_matrix=SVD.fit_transform(transpose)
    correlation_data=np.corrcoef(resultant_matrix)
    place_names=rating_tabular_data.columns
    place_list=list(place_names)
    index=place_list.index(place_name)
    corr_column=correlation_data[index]
    return list(place_names[(corr_column<1.0) & (corr_column>0.6)])