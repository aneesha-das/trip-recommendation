# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 10:15:24 2020

@author: Aneesha
"""

import pandas as pd
import numpy as np
data=pd.read_csv("place_recommendation_raw_data.csv")
data_copy=data.copy(deep=True)
place_list=[];
data_copy.drop_duplicates(subset=['Name','Age Range', 'Place 1 (from India)'], keep='first', inplace=True)
data_copy=data_copy.reset_index()
# replacing dirty values
cols=('Place 1 (from India)', 'Place 2(from India)', 'Place 3(from India)', 'Place 4(from India)', 'Place 5(from India)', 'Place 6(from India)', 'Place 7(from India)', 'Place 8(from India)', 'Place 9(from India)', 'Place 10(from India)')
for col in cols:
    replaced_places={"St. Paul's Cathedral": "St. Pauls Cathedral",'Victoria ':'Victoria Memorial','Uttaranchal':'Uttarakhand','Thirupathi':'Tirupati Temple','Shantiniketan':'Santiniketan','shantiniketan':'Santiniketan','North-East':'North East','Lahaul (Himachal Pradesh)':'Lahaul And Spiti Valley','Kota, Rajasthan':'Kota','Kashmir ':'Jammu and Kashmir','Jammu ':'Jammu and Kashmir','Duars':'Dooars','Guwahati, Assam':'Guwahati','Bhubaneshwar':'Bhubaneswar','Bakura ':'Bankura','allhabad':'Allahabad','Ajanta-Ellora (Maharashtra)':'Ajanta Ellora Caves','gujrat':'Gujarat','Varanashi':'Varanasi','Ranchi waterfall':'Ranchi','Peling':'Pelling','Nim pith':'Numpith','Mumbai, goa':'Goa','Kamaksha Temple':'Kamakhya Temple','Ghoom, West Bengal':'Darjeeling','Daman':'Daman and Diu','Dadar and nagar haweli':'Dadranagar haveli','Bangalore ':'Bangalore','Allepy':'Alappuzha','Tirupati':'Tirupati Temple','Tawang':'Arunachal Pradesh','Tarapit':'Tarapith','Harshil valley':'Harsil Valley','Banglor':'Bangalore','Bandiur':'Bandipur National Park','Arrakku valley':'Araku Valley','rajasthan jaisalmer':'Jaisalmer','Ranghar, Talata ghar, Assam':'Assam','Murshidabad, West Bengal':'Murshidabad','Mondarmoni':'Mandarmani','Missouri':'Mussoorie','Lava Lolegaon':'Lava','Kumaun Himalaya (Uttarakhand)':'Uttarakhand','Kulu manali':'Manali','Kaziranga':'Kaziranga National Park','Chakdha ':'Chakdaha','Benaras':'Varanasi','Banglore':'Bangalore','Ayodhya Hills, West Bengal':'Purulia','Vaizag':'Visakhapatnam','Hazaar Duari':'Murshidabad','Garhwal Himalaya (Uttarakhand)':'Uttarakhand','Dakshineshwar':'Dakshineswar Kali Temple','Chikmagalur':'Chikmagalur','Baroda':'Vadodara','Chadipur':'Chandipur','Uttarakhand kedarnath':'kedarnath','Kochin':'Kochi','Jaydev Kenduli':'Joydev Kenduli','Hydrabad':'Hyderabad','Gajaburu Hills, Purulia':'Purulia','Bhaisak':'Visakhapatnam','Bengaluru':'Bangalore','Bankura, West Bengal':'Bankura','Bangaluru':'Bangalore','Agara':'Agra','Yuksom':'Sikkim','Srinagar':'Jammu And Kashmir','Puruliea':'Purulia','Podicherry':'Pondicherry','Northeast (Meghalaya)':'Meghalaya','Kigwema, Nagaland':'Nagaland','New Delhi':'Delhi','Mysuru':'Mysore','Mandarmoni':'Mandarmani','Lahaul':'Lahaul And Spiti Valley','Kalinpong':'Kalimpong','Dakhineswar Temple ':'Dakshineswar Kali Temple','Chaina town ':'China Town','Pehalgaon ':'Pahalgam','Arunachal':'Arunachal Pradesh','Vishakapatnam':'Visakhapatnam','Umed Bhawan palace ':'Umaid Bhawan Palace','Spiti (Himachal Pradesh)':'Lahaul And Spiti Valley','Corbett':'Jim Corbett National Park','Bakura':'Bankura','Vishakhapattanam':'Visakhapatnam','Vishakapattanam':'Visakhapatnam','Vishakhapatnam':'Visakhapatnam','Vizag':'Visakhapatnam','Moti jheel (Murshidabad)':'Murshidabad','Simla':'Shimla','Mandermani':'Mandarmani','Kinnaur (Himachal Pradesh)':'Kinnaur','Baghini Glacier':'Bagini Glacier','Andaman and Nicobar Island':'Andaman','Ichapur ':'Ichapur','Leh':'Leh Ladakh','Kerela':'Kerala','himachal ':'Himachal Pradesh','Nainitaal':'Nainital','Kazironga national park':'Kaziranga National Park','Andamans':'Andaman','Bhubaneshwar ':'Bhubaneswar','Jammu & kashmir':'Jammu and Kashmir','Kashmir':'Jammu and Kashmir', 'Jammu':'Jammu and Kashmir','Hazaar Duari (Murshidabad)':'Murshidabad', 'Berhampore':'Murshidabad','Dooers':'Dooars','banaras':'Varanasi','Dadra And Nagar Haveli':'Dadranagar haveli','Hampi, Karnataka':'Hampi', 'Gantok':'Gangtok', 'North sikim':'Sikkim', 'North Sikkim':'Sikkim', 'Sandakfu':'Sandakphu', 'katra(Vaishno Devi)':'Vaishno Devi, Katra'}
    data_copy[col].replace(replaced_places, inplace=True)
    data_copy[col] = data_copy[col].apply(lambda x: x.strip())
    data_copy[col]=data_copy[col].apply(lambda x:x.title())
    place_list.append(data_copy[col])
place_list=np.unique(place_list)
data_copy.replace("Na", np.nan, inplace=True)
data_copy.drop(columns=['index'],inplace=True)
data_copy.to_csv("place_recommendation_place_filtered.csv", index=False)
place_list = np.delete(place_list, [129])
ids=np.arange(start=1,stop=len(place_list)+1,step=1,dtype=int)
places=pd.DataFrame({
        'id':ids,
        'name':place_list
    })
places.to_csv('places.csv', index=False)