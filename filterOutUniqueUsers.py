# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:43:32 2020

@author: Amit
"""

import pandas as pd
import numpy as np
data=pd.read_csv("temporary_working_documents/place_recommendation_place_filtered.csv")
data_copy=data.copy(deep=True).to_numpy()
user_list=[];
user_data=data_copy[:,1:5]
for user in user_data:
    user_name=user[0]
    user_age=user[1]
    user_gender=user[2]
    user_state=user[3]
    user_list.append([user_name,user_age,user_gender,user_state])
ids=np.arange(start=1,stop=len(user_list)+1,step=1,dtype=int)
user_list=np.insert(user_list,0,ids,axis=1)
users=pd.DataFrame(user_list,columns=['id','name','age','gender','state'])
users.to_csv('users.csv', index=False)