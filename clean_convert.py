# -*- coding: cp1252 -*-
#round 2

import csv


def main():
    dic_of_coors = make_dict()
    #test(dic_of_coors)
    write_to_geojson(dic_of_coors)


def write_to_geojson(a_dict):
    geo_file = open("mpas.geojson","w")
    geo_file.write('{\n')#  1{
    geo_file.write('"type": "FeatureCollection",\n')
    geo_file.write('"features": [\n')#1[
    geo_file.write('{\n')#  2{
    geo_file.write('"type": "Feature", "properties": { ')
    #need to automate from here
    geo_file.write('"name" : "Laguna Beach State Marine Reserve (SMR)"},')
    geo_file.write('"geometry": { "type": "Polygon", "coordinates": [[')# 3{
    #iterating through dic
    k = 0
    s = ""
    for i in a_dict:
        s = a_dict[k]
        geo_file.write(str(s) + ",")
        k+=1
    geo_file.write(str(a_dict[0])+"]]}}]}\n")
    geo_file.close()


def make_dict():
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
        sub_lon = round(((float(sub_lon))/60),6)
        lon = lon[0:3]
        lon = float(lon)+sub_lon
        lon = lon * -1

        #adding both to a dict. Key auto generated
        coor_list = [lon,lat]
        coor_dict[key] = coor_list
        key+=1
    return coor_dict

def write_to_csv(some_dict):
    key = 0
    with open('dict.csv','wb') as csv_file:
        writer = csv.writer(csv_file)
        for i in some_dict:
            writer.writerow(some_dict[key])
            key+=1

def test(some_dict):
    k = 0
    for i in some_dict:
        print some_dict[k]
        k+=1

def pull_from_csv():
    mpas = {}
    name = ""
    not_name = ""
    test = open('dict.csv','r')
    for line in test:
        for letter in line:
            if letter == ",":
                print name
                return name
            else:
                name = name + letter
    
    
        
        
pull_from_csv()





main()
