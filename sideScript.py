# -*- coding: cp1252 -*-

mpa_name= ""
lat = ""
lon = ""

coor = 'coordinates.txt'
check = open(coor,'r')

for line in check:
   for char in line:
      if (int(char) != int(char)) and (char != "*" or char !=";" or char != "." or char!= "'"):
         mpa_name = str(mpa_name) + str(char)

print mpa_name
