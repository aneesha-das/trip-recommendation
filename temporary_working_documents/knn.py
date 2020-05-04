# -*- coding: utf-8 -*-
"""
Created on Sun May  3 20:21:45 2020

@author: Amit
"""

import numpy as np
import pandas as pd
import sklearn
from sklearn.neighbors import NearestNeighbors

place_tag_mapping=pd.read_csv("place_tag_mapping.csv")
place_details=pd.read_csv("places.csv")
tags=pd.read_csv("tags.csv")
tag_names=np.array(tags['name'])
place_columns=np.array(place_details.columns)
combined_columns=np.concatenate((place_columns,tag_names))
place_with_tags=place_details.merge(place_tag_mapping,left_on='id',right_on="place_id")
place_tag_matrix=[]
row=[]
tag_list=list(np.array(tags['id']))
place_name_list=list(np.array(place_details['name']))
place_id_list=list(np.array(place_details["id"]))
for i in range(0,51):
    row.append(0)
added_places=[]
for index in range(0,place_with_tags["id"].size):
    if place_with_tags["id"][index] not in added_places:
        place_tag_matrix.append(row.copy())
        added_places.append(place_with_tags["id"][index])
    place_tag_matrix[place_with_tags["id"][index]-1][tag_list.index(place_with_tags["tag_id"][index])]=1


places_df=pd.DataFrame(place_tag_matrix,columns=tag_names)

liked_place_name="Himachal Pradesh"
liked_place=places_df.iloc[place_name_list.index(liked_place_name),:].copy(deep=True)
nbrs=NearestNeighbors(n_neighbors=5).fit(places_df)
nearest_matches=nbrs.kneighbors([liked_place])
match_indexes=nearest_matches[1][0]
print(liked_place)
for index in match_indexes:
    recommended_place_id=place_details["id"][index]
    print(place_details.iloc[recommended_place_id-1,:])