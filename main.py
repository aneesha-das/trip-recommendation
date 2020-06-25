# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:47:20 2020

@author: Amit
"""


from utils.contentBasedFilterUtils import getTopRecommendations,generateRelevantPlacesWithReviews,getPlaceNameById
from utils.collabFilterUtils import getCollabFilteringRecommendations,getUserWiseCollabFilteringRecommendations
import numpy as np
import pandas as pd

places=[]
placesLiked=[
        {"name":"Manali","rating":10},
        {"name":"Goa","rating":10},
        {"name":"Darjeeling","rating":6},
        {"name":"Jamshedpur","rating":1},
        {"name":"Ooty","rating":9},
        {"name":"Rajasthan","rating":7},
        {"name":"Dehradun","rating":6},
        {"name":"Delhi","rating":4},
        {"name":"Agra","rating":5},
        {"name":"Kolkata","rating":7}
        ]
userId=1
places_data=[]
for i in range(1,195):
    places_data.append(0)
for placeLiked in placesLiked:
    if placeLiked["rating"]>5:
        places_data=np.add(places_data,np.array(generateRelevantPlacesWithReviews(placeLiked["name"],"cosine"))*placeLiked["rating"])
    

for index in range(1,195):
    placeId=index
    places.append({"id":placeId,"correlation":places_data[index-1]})
    
places
places.sort(key=lambda x: x["correlation"], reverse=True)
places=places[:70]

places_rows=[]
place_ids=[]
for place in places:
    place_ids.append(place["id"])
    places_rows.append({"id":place["id"],"name":getPlaceNameById(place["id"])})
    
places_rows.sort(key=lambda x: x["id"], reverse=False)

rating_data=pd.read_csv('user_place_mapping.csv')
filtered_ratings=[]
for index in rating_data.index:
    if rating_data["place_id"][index] in place_ids:
        filtered_ratings.append({"user_id":rating_data["user_id"][index],"place_id":rating_data["place_id"][index],"rating":rating_data["rating"][index]})
places_df=pd.DataFrame(places_rows)
places_df.to_csv('temp_places.csv', index=False)
ratings_df=pd.DataFrame(filtered_ratings)
ratings_df.to_csv('temp_ratings.csv', index=False)
getUserWiseCollabFilteringRecommendations(userId)

#print(getCollabFilteringRecommendations("Darjeeling"))