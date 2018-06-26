# -*- coding: cp1252 -*-
#round 2

import csv

def main():
    dic_1 = pull_from_csv()
    dic_of_coors = clean_data(dic_1)
    #test(dic_of_coors)
    write_to_geojson(dic_of_coors)

def test(some_dict):
    for i in some_dict:
        print some_dict[i]

def write_to_geojson(a_dict):
    geo_file = open("mpas.geojson","w")
    geo_file.write('{\n')#  1{
    geo_file.write('"type": "FeatureCollection",\n')
    geo_file.write('"features": [\n')#1[
    #need to automate from here
    x = 0
    for k in a_dict:
        geo_file.write('{\n')#  2{
        geo_file.write('"type": "Feature", "properties": { ')

        l = str(k)
        smt = str(k[-5:-1])
       
        geo_file.write('"name" : "'+l+'","type" : "'+str(smt)+'" },')
        geo_file.write('"geometry": { "type": "Polygon", "coordinates": [')
        geo_file.write(str(a_dict[k]))
        fail = len(a_dict)
        x+=1
        if x == fail:
            geo_file.write(']}}')
        elif x!=fail:
            geo_file.write(']}},')  
    geo_file.write(']}')
    
    geo_file.close()

def pull_from_csv():
    mpas = {}
    coors = []
    with open('dict.csv','rb') as coordinate_file:
        local_reader = csv.reader(coordinate_file, delimiter=',')
        for row in local_reader:
            size = len(row)
            x = 1
            while x != size:
                coors.append(row[x])
                x+=1
            mpas[row[0]] = coors
            coors = []
    coordinate_file.close()
    return mpas
            
def clean_data(raw_coors):
    coors = []
    lat = ''
    sub_lat = ''
    
    lon = ''
    sub_lon = ''

    clean_coors = []
    clean_dict = {}
    for mpa_name in raw_coors:
        coors = raw_coors[mpa_name]
        for element in coors:
            lat = float(element[0:2])
            sub_lat = float(element[4:10])
            sub_lat = sub_lat/60
            lat = round(lat+sub_lat,4)
            #lat part

            lon = float(element[20:23])
            sub_lon = float(element[25:31])
            sub_lon = sub_lon/60
            lon = round(-1*(lon+sub_lon),4)
            #lon part

            
            placeholder = [lon,lat]
            clean_coors.append(placeholder)
            placeholder = []
        clean_dict[mpa_name] = clean_coors

        clean_coors = []

    return clean_dict
            
            


main()







