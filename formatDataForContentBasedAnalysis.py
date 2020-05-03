# -*- coding: utf-8 -*-
"""
Created on Sun May  3 19:38:33 2020

@author: Aneesha
"""


import pandas as pd

place_tag_mapping=pd.read_csv("place_tag_mapping.csv")
tags=pd.read_csv("tags.csv")
place_tag_mapping=place_tag_mapping.merge(tags,left_on='tag_id',right_on="id")
df=place_tag_mapping.groupby("place_id")['name'].unique()