# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:38:33 2020

@author: Aneesha
"""


import pandas as pd
def getPlaces():
    place_tag_mapping=pd.read_csv("place_tag_mapping.csv")
    place_details=pd.read_csv("places.csv")
    tags=pd.read_csv("tags.csv")
    place_tag_mapping=place_tag_mapping.merge(tags,left_on='tag_id',right_on="id")
    places=place_tag_mapping.groupby("place_id")['name'].unique()
    places=places.to_frame()
    places['name']=places['name'].apply(lambda x:' '.join(x))
    places=place_details.merge(places,left_on='id',right_on="place_id")
    places.rename(columns={'name_x':'name','name_y':'tags'}, inplace=True)
    return places.copy(deep=True)