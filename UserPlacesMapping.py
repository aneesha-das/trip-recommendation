# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 23:08:10 2020

@author: Amit
"""

import pandas as pd
import numpy as np
data=pd.read_csv("place_recommendation_place_filtered.csv")
data_copy=data.copy(deep=True).to_numpy()
user_list=[];
place_data=data_copy[:,5:25]
user_list=data_copy[:,1]
places=pd.read_csv("places.csv")
data_copy=places.copy(deep=True).to_numpy()
users=pd.read_csv("users.csv")
users_data_copy=users.copy(deep=True).to_numpy()

def getPlaceId(place_name):
    place_id=0
    for place in data_copy:
        if(place[1]==place_name):
            place_id=place[0]
            break
    return place_id

def getUserId(user_name):
    user_id=0
    for user in users_data_copy:
        if(user[1]==user_name):
            user_id=user[0]
            break
    return user_id

user_id=1
mapping=[]
for user_place_with_rating in place_data:
    for i in range(0,20,2):
        place_id=getPlaceId(user_place_with_rating[i])
        if(place_id!=0):
            mapping.append([user_id,place_id,user_place_with_rating[i+1]])
    user_id+=1
userPlaceMapping=pd.DataFrame(mapping,columns=['User Id','Place Id','Rating'])
userPlaceMapping.to_csv('user_place_mapping.csv', index=False)