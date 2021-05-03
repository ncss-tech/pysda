# -*- coding: utf-8 -*-
"""
Created on Mon May  3 08:48:19 2021

@author: Charles.Ferguson
"""

import sys, os

# supply the directory with the fetch.py script
sys.path.append(r'D:\GIS\TOOLBOXES\pysda')

# import the fetch.py script that 
# makes the call to Soil Data Access
import fetch as sda

# specify your polygons (shapefile, geopackage, filegdb)
myshp = r'C:\Temp\sda_call_ex.shp'

# make the call
# shp = myshp
# meta = False
# export = True if you want to write the results to disk, same format in WGS84
# name = results name
soils = sda.shp(shp = myshp, meta = False, export= True, name = 'my_soils')
