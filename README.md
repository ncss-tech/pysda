# pysda
 
The purpose of this repository is intended to expose the functionality of Soil Data Access within python as a readily available tool waiting to be called upon.  It was inspired by the work of soilDB, sharpShootR, ... pysda enables you to get answers from SSURGO related questions quickly without any additional COTS or GUI driven software.

Currently users can submit for both tabular and spatial data.  The results are returned to a (geo)pandas data frame, and spatial data can optionally be exported the same location as the source of the AOI.  AOIs can be provided as shapefile, geopackage layers, ESRI file geodatabase feature class, or WKT string.  Exports of spatial data DO NOT go back to ESRI file geodatabases, they are written to the parent directory of the geodatabse.  All spatial data submitted to Soil Data Access must be in EPSG 4326 (WGS84) and will be transformed if need be.  This is what Soil Data Access returns.

Soil Data Access is restricted to how many characters it will return, ~ 10 million. That adds up quickly with coordinate pairs and precision.  It's generally safe to assume that you could grab a standards U.S. county but it all really depends on the polygon and vertex density.  When the limit has been exceeded or the Soil Data Access timesout has been reached, there is no HTTP error, it will return an empty JSON string.  This raises a Value Error (JSONDecodeError).

More to come...

https://sdmdataaccess.nrcs.usda.gov/Default.aspx
