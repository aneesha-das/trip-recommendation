# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:38:33 2020

@author: Aneesha
"""


import pandas as pd

def getPlaces():
    place_tag_mapping=pd.read_csv("place_tag_weights.csv")
    place_details=pd.read_csv("places.csv")
    tags=pd.read_csv("tags.csv")
    tag_ids=tags['id']
    place_tag_names=place_tag_mapping.merge(tags,left_on='tag_id',right_on="id")
    place_tag_names=place_tag_names.groupby("place_id")['name'].unique().to_frame()
    place_tag_names['tags']=place_tag_names['name'].apply(lambda x:' '.join(x))
    place_tags=place_tag_mapping.groupby("place_id")['tag_id'].apply(list).to_frame()
    place_weights=place_tag_mapping.groupby("place_id")['weight'].apply(list).to_frame()
    places=place_tags.merge(place_weights, on='place_id')
    places=place_details.merge(places, left_on='id', right_on='place_id')
    places=places.merge(place_tag_names, left_on='id', right_on='place_id')
    places_indices=places.index
    place_tag_vector=[]
    for index in places_indices:
        weight_tags=[]
        for tag in tag_ids:
            tag_list=places.at[index,'tag_id']
            if(tag in tag_list):
                weight_tags.append(places.at[index,'weight'][tag_list.index(tag)])
            else:
                weight_tags.append(0)
        place_tag_vector.append([places.at[index, 'id'],places.at[index, 'name_x'],places.at[index,'tags'],weight_tags])
    place_tags=pd.DataFrame(place_tag_vector,columns=['id','name','tags','weight'])
    return place_tags.copy(deep=True)
