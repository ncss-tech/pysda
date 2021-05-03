# pysda
 
The purpose of this repository is intended to expose the functionality of Soil Data Access within python as an readily available tool waiting to be called upon.  It was inspired by the woork of soilDB, sharpShootR, ...  Python users no longer have to be jealous of the R folks when they want answers quick.

Currently users can submit for both tabular and spatial data.  The results are returned to a (geo)pandas data frame, and spatial data can optionally be exported the same location from where the AOI came from that was passed to the script.  AOIs can be provided as shapefile, geopackage layers, fille, ESRI file geodatabase feature class, or WKT string.  All spatial data submitted to Soil Data Access must be in EPSG 4326 (WGS84).  This is what Soil Data Access returns.

Soil Data Access is is restricted to how many characters it will return, ~ 10 million which seems like a lot but all of the vertices from the soil polygons with their precision add up quickly.  It's generally safe to assume that you could grab a standards U.S. county but it all really depends on the polygon and vertex density.

When the limit has been exceeded or Soil Data Access timesout has been reached, there is no HTTP error, it will return an empty JSON string.  This is raises a Value Error (JSONDecodeError).

More to come...

