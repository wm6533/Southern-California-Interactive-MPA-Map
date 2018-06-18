# -*- coding: cp1252 -*-

import csv

dumb_list = ["33° 33.224' N. lat. 117° 49.184' W. long.;","33° 30.211' N. lat. 117° 49.200' W. long.;","33° 30.713' N. lat. 117° 49.200' W. long.; and","33° 30.713' N. lat. 117° 45.264' W. long."]

lat = ""
sub_lat=''
lon = ""
sub_lon=''
key = 0
coor_list=[]

coor_dict = {}

for value in dumb_list:
    #handling lat
    lat = value[0:10]
    sub_lat = lat[4:10]
    sub_lat = round((float(sub_lat)/60),6)
    lat = lat[0:2]
    lat = float(lat)
    lat = lat + sub_lat


    #handling lon
    lon = value[20:40]
    sub_lon = lon[5:11]
    sub_lon = round((float(sub_lon)/60),6)
    lon = lon[0:3]
    lon = float(lon)+sub_lon

    #adding both to a dict. Key auto generated
    coor_list = [lat,lon]
    coor_dict[key] = coor_list
    key+=1

key = 0
with open('dict.csv','wb') as csv_file:
    writer = csv.writer(csv_file)
    for i in coor_dict:
        writer.writerow(coor_dict[key])
        key+=1
