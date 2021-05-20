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

# now to get SSURGO property, sandtotal_r
wtdavg=sdaprop.getprop(df=myaoi,column='mukey',method='wtd_avg',top=0,bottom=100,prop='sandtotal_r',minmax=None,prnt=False,meta=False)

# now join/merge the results, show first record
mymerge = myaoi.merge(wtdavg, how = 'inner', on = 'mukey')
mymerge.head(1)

# visualize
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
fig.set_size_inches(5,5)
mymerge.plot(column = 'sandtotal_r', ax=ax, cmap = 'rainbow',
            legend = True)

# add a legend
leg = ax.get_legend()
leg.set_bbox_to_anchor((1.4,1.0))
ax.set(title = 'Total Sand - Weighted Average \n 0 - 100 cm')

plt.show()