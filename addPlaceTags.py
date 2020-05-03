# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:25:45 2020

@author: Aneesha
"""
import pandas as pd
import numpy as np

def findTagId(placeName):
    for x in tags.to_numpy():
        if(x[1]==placeName):
            return x[0]
    return 0;


data=pd.read_csv("temporary_working_documents/places_tag.csv")
data_copy=data.copy(deep=True)
data_copy.replace(np.nan, '?', inplace=True)
place_list=[];
tag_list=[];
place_tag=[];
for x in range(1,22,1):
    col='tag'+str(x)
    tag_list.append(data_copy[col])
tag_list=np.unique(tag_list)
tag_list = np.delete(tag_list, [0])
# print(tag_list)
ids=np.arange(start=1,stop=len(tag_list)+1,step=1,dtype=int)
tags=pd.DataFrame({
        'id':ids,
        'name':tag_list
    })
tags.to_csv('tags.csv', index=False)
place_data=data_copy.to_numpy()
mapping=[]
for place_with_tag in place_data:
    for i in range(2,23,1):
        if(place_with_tag[i]!="?"):
            tag_id=findTagId(place_with_tag[i])
            if(tag_id==0):
                print(place_with_tag[i])
            mapping.append([place_with_tag[0],tag_id])
tagPlaceMapping=pd.DataFrame(mapping,columns=['place_id','tag_id'])
tagPlaceMapping.to_csv('place_tag_mapping.csv', index=False)