# -*- coding: utf-8 -*-
"""
Created on Fri May 14 12:39:29 2021

@author: Charles.Ferguson
"""

import sys

sys.path.append(r"d:\gis\toolboxes\pysda")

import sdapoly, sdaprop, sdainterp


myshp = r"F:\ZBOOK\GIS\TEMP\fs.shp"
myaoi = sdapoly.shp(myshp, export = True, name = 'fto2.shp')

test_aoi = sdapoly.gdf(myaoi)

wtdavg = sdaprop.getprop(df = myaoi, column ='mukey', method = 'wtd_avg', top = 0, bottom = 100, prop = 'sandtotal_r', minmax = None, prnt=False, meta = False)
domcompnum = sdaprop.getprop(myaoi, 'mukey', 'claytotal_r', method = 'dom_comp_num', top = 300, bottom = 400, prnt = False)
minmax = sdaprop.getprop(myaoi, 'mukey', 'claytotal_r', method = 'minmax', top = 20, bottom = 55, minmax = 'MAX', prnt = False)
domcond = sdaprop.getprop(myaoi, 'mukey', 'taxorder', method = 'dom_cond', prnt = False)
domcompcat = sdaprop.getprop(myaoi, 'mukey', 'drainagecl', method = 'dom_comp_cat', prnt = False)

intdomcomp = sdainterp.getinterp(myaoi, 'mukey', 'WMS - Pond Reservoir Area', 'dom_comp')
intwta = sdainterp.getinterp(myaoi, 'mukey', 'Ground Penetrating Radar Penetration', 'wtd_avg')
intdomcond = sdainterp.getinterp(myaoi, 'mukey', 'ENG - Shallow Excavations', method = 'dom_cond', prnt = True)

import pandas as pd, geopandas as gpd
myaoi = myaoi.merge(wtdavg, how='inner', on='mukey')
