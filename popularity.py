# -*- coding: utf-8 -*-
"""
Created on Wed May  6 22:30:32 2020

@author: Amit
"""

import pandas as pd
import numpy as np

places=pd.read_csv('places.csv')
ratings=pd.read_csv('user_place_mapping.csv')
place_ratings=pd.merge(places,ratings,left_on='id',right_on='place_id')[["id","name","user_id","rating"]]
rating_count=pd.DataFrame(place_ratings.groupby('id')['rating'].count())
sorted_ratings=rating_count.sort_values('rating',ascending=False).head(10)
print(pd.merge(places,sorted_ratings,on="id").sort_values('rating',ascending=False))