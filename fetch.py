# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:45:45 2021

@author: Charles.Ferguson
"""
class Terminate(Exception):
    pass

def msg(s):
    print(s)
    
def tab(q, meta = False):

    theURL = "https://sdmdataaccess.nrcs.usda.gov"
    theURL = theURL + "/Tabular/SDMTabularService/post.rest"
    
    rDic = {}
    
    if meta:
        rDic["format"] = "JSON+COLUMNNAME+METADATA"
    else:
        rDic["format"] = "JSON+COLUMNNAME"
    
    rDic["query"] = q
    rData = json.dumps(rDic)
    
    results = requests.post(data=rData, url=theURL) 
    
    qData = results.json()
        
    cols = qData.get('Table')[0]
    data = qData.get('Table')[1:]
        
    df = pd.DataFrame(data, columns = cols)
        
    return df
        

def wkt(wkt=str, meta=False):
    
    """Grab SSURGO geometry from user define AOI in wkt format
    
    :param str wkt: the wkt representation of the AOI extent\n
    :param boolen meta: get the column metadata returned in the JSON string, only suitable for arcgis features classes:
    :return: SSURGO spatial data in wkt format"""
    
    q = """~DeclareGeometry(@aoi)~

    select @aoi = geometry::STPolyFromText('""" + wkt + """' , 4326)

    ~DeclareIdGeomTable(@outtable)~
    ~GetClippedMapunits(@aoi,polygon,geo,@outtable)~
    
    select *
    into #temp
    from @outtable;
    
    select areasymbol, areaname, muname, musym, mukey, nationalmusym as nat_musym, geom
    from #temp, legend, mapunit
    where #temp.id = mapunit.mukey and mapunit.lkey = legend.lkey"""
    
    # print(q)
    
    try:
        theURL = "https://sdmdataaccess.nrcs.usda.gov"
        theURL = theURL + "/Tabular/SDMTabularService/post.rest"
        
        rDic = {}
        
        if meta:
            rDic["format"] = "JSON+COLUMNNAME+METADATA"
        else:
            rDic["format"] = "JSON+COLUMNNAME"
        
        rDic["query"] = q
        rData = json.dumps(rDic)
        
        results = requests.post(data=rData, url=theURL)
        # print('results are next')
        # print(results)
        qData = results.json()
        
        cols = qData.get('Table')[0]
        data = qData.get('Table')[1:]
    
        df = pd.DataFrame(data, columns = cols)
        geometry = df['geom'].map(shapely.wkt.loads)
        gdf = gpd.GeoDataFrame(df, crs = "EPSG:4326", geometry = geometry)
    
        #gdf = gpd.GeoDataFrame(df, geometry='geom')
        
        return gdf
        
    
    except (exceptions.InvalidURL, exceptions.HTTPError, exceptions.Timeout):
        print('Requests error, Soil Data Access offline??')
    
        
    except JSONDecodeError as err:
        print('JSON Decode error: ' + err.msg)
        print('This usually happens when the extent is too large, try smaller extent.')
     
    
    except Exception as e:
        print('Unhandled error')
        print(e)
       
    

def shp(shp=str, meta=False, export=False, name=None):
    
    """Grab SSURGO soil polygons using input shp for extent
    
    :str shp: path to shp file for AOI
    :boolean meta: get the column metadata returned in the JSON string, only suitable for arcgis features classes:\n
    :boolean export: write results to source directory
    :str name: provide a name with, if None, SSURGO_WGS84.shp used
    :return: geopandas data frame epsg 4326"""
    
    err = None
    
    if not shp.endswith(".shp"):
        err = 'input shp '  + shp + ' does not appear to be a shapefile'
        raise TypeError(err)

    else:
        gdf = gpd.read_file(shp)
    
    if not gdf.crs == 'WGS 84':
         msg('Transforming shp to WGS 84')
         gdf = gdf.to_crs("EPSG:4326")
    
    if len(gdf) > 1:
        dVal = 1
        gdf['df'] = dVal
        gdf = gdf.dissolve(by = 'df')
        
    # make the smallest request possible
    hull = gdf["geometry"].convex_hull
    wkt_str = hull.geometry.to_string(index = False, header = False)
    
    hull_soils = wkt(wkt_str)
    
    result = gpd.clip(hull_soils, gdf)
    
    if export:
        
        result.drop(['geom'], axis = 1, inplace=True)
        
        dest = os.path.dirname(shp)
        
        if name is not None:
            if not name.endswith('.shp'):
                name = name + '.shp'
            
        else:
            name = 'SSURGO_WGS84.shp'
    
        result.to_file(os.path.join(dest, name))
    
    else:
        pass
    
    return result
        
    

def gpkg(gpkg=str, layer=str, meta=False, export=False, name=None):
    
    """Grab SSURGO soil polygons using input geopackage layer for extent
    
    :str gpkg: path to geopackage\n
    :str layer: layer to use for extent\n
    :boolean meta: column metadata returned in JSON string, arcgis features classes only\n
    :boolean export: write results to source geopackage\n
    :str name: output layer name with, if None SSURGO_WGS8 used\n
    :return: geopandas data frame epsg 4326"""
    
    gdf = gpd.read_file(filename=gpkg, layer=layer)
    
    if not gdf.crs == 'WGS 84':
        msg('Transforming shp to WGS 84')
        gdf = gdf.to_crs("EPSG:4326")
        
    if len(gdf) > 1:
        dVal = 1
        gdf['df'] = dVal
        gdf = gdf.dissolve(by = 'df')
    
    # make the smallest request possible
    hulls = gdf["geometry"].convex_hull
    wkt_str = hulls.geometry.to_string(index = False, header = False)
    hull_soils = wkt(wkt=wkt_str)
    
    result = gpd.clip(env_soils, gdf)
    
    if export:
        
        result.drop(['geom'], axis = 1, inplace=True)
        
        if name is None:
            name = "SSURGO_WGS84"  
    
        result.to_file(gpkg, layer=name, driver="GPKG")
    
    else:
        pass
            
    
    return result

def fgdb(gdb=str, layer=str, meta=False, export=False, name=None):
    
    """Grab SSURGO soil polygons using file geodatabse layer for extent
    
    :str gdb: path to file geodatabase\n
    :str layer: layer to use for extent\n
    :boolean meta: column metadata returned in JSON string, arcgis features classes only\n
    :boolean export: write a .shp result to parent directory of the file geodatabse\n
    :str name: output layer name with, if None SSURGO_WGS8 used\n
    :return: geopandas data frame epsg 4326"""
    
    # get layerindex
    lyrs = fiona.listlayers(gdb)
    idx = lyrs.index(layer)
   
    gdf = gpd.read_file(filename=gdb, layer=idx)
   
    if not gdf.crs == 'WGS 84':
        msg('Transforming shp to WGS 84')
        gdf = gdf.to_crs("EPSG:4326")
    
    if len(gdf) > 1:
        dVal = 1
        gdf['df'] = dVal
        gdf = gdf.dissolve(by = 'df')
    
    # make the smallest request possible    
    hulls = gdf["geometry"].convex_hull
    wkt_str = hulls.geometry.to_string(index = False, header = False)            
    hull_soils = wkt(wkt=wkt_str)
    
    result = gpd.clip(hull_soils, gdf)

    
    if export:
        
        dest = os.path.dirname(gdb)
        
        result.drop(['geom'], axis = 1, inplace=True)
        
        if name is None:
            name = "SSURGO_WGS84"  
    
        result.to_file(dest, layer=name)
    
    
    return result
     
    
    
import sys, os, json, requests, pandas as pd, geopandas as gpd, shapely, fiona
from shapely import wkt as swkt

from json.decoder import JSONDecodeError
from requests import exceptions

# wkt strings are long...
pd.set_option('display.max_colwidth', None)



