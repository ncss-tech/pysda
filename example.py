# -*- coding: utf-8 -*-
"""
Created on Mon May  3 08:48:19 2021

@author: Charles.Ferguson
"""

import sys
import matplotlib.pyplot as plt

sys.path.append(r"d:\gis\toolboxes\pysda")

# import pysda
import sdapoly, sdaprop, sdainterp

# get/set an aoi
myshp = r"F:\ZBOOK\GIS\TEMP\fs.shp"
myaoi = sdapoly.shp(myshp)

myaoi.plot()

# get SSURGO property, sandtotal_r
wtdavg=sdaprop.getprop(df=myaoi,column='mukey',method='wtd_avg',top=0,bottom=100,prop='sandtotal_r',minmax=None,prnt=False,meta=False)

# remove duplicate columns, join/merge the results, show first record
myaoi_cols = myaoi.columns.tolist()
wtdavg_cols = wtdavg.columns.tolist()
drop_cols = [col for col in wtdavg_cols if col in myaoi_cols and col != 'mukey']
wtdavg.drop(columns = drop_cols, inplace = True) 


mymerge = myaoi.merge(wtdavg, how = 'inner', on = 'mukey')
mymerge.head(1)

# visualize
fig, ax = plt.subplots(1,1)
fig.set_size_inches(5,5)
mymerge.plot(column = 'sandtotal_r', ax=ax, cmap = 'rainbow',
            legend = True)

# add a legend
leg = ax.get_legend()
leg.set_bbox_to_anchor((1.4,1.0))
ax.set(title = 'Total Sand - Weighted Average \n 0 - 100 cm')

plt.show()