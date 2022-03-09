# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 11:45:45 2021

@author: Charles.Ferguson
"""
class Terminate(Exception):
    pass

def msg(s):
    print(s)

# this function was migrated to the module sdatab.tabular
# def tab(q, meta = False):
    
#     import json, requests, pandas as pd
#     from json.decoder import JSONDecodeError
#     from requests import exceptions
    
#     try:

#         theURL = "https://sdmdataaccess.nrcs.usda.gov"
#         theURL = theURL + "/Tabular/SDMTabularService/post.rest"
        
#         rDic = {}
        
#         if meta:
#             rDic["format"] = "JSON+COLUMNNAME+METADATA"
#         else:
#             rDic["format"] = "JSON+COLUMNNAME"
        
#         rDic["query"] = q
#         rData = json.dumps(rDic)
        
#         results = requests.post(data=rData, url=theURL) 
        
#         qData = results.json()
            
#         cols = qData.get('Table')[0]
#         data = qData.get('Table')[1:]
            
#         df = pd.DataFrame(data, columns = cols)
            
#         return df
    
#     except (exceptions.InvalidURL, exceptions.HTTPError, exceptions.Timeout):
#         print('Requests error, Soil Data Access offline??')
        
#     except JSONDecodeError as err:
#         print('JSON Decode error: ' + err.msg)
#         print('This usually happens when the extent is too large, try smaller extent.')
     
    
#     except Exception as e:
#         print('Unhandled error')
#         print(e)
        

def sdaCall(gdf, meta=False):
     
    import json, requests, geopandas as gpd, pandas as pd, shapely
    from json.decoder import JSONDecodeError
    from requests import exceptions
    
    pd.set_option('display.max_colwidth', None)
    
    
    invalid = ['POINT','MULTIPOINT','LINESTRING','MULTILINESTRING']    
    gtype = [g.upper() for g in gdf.geom_type.to_list()]
    
    test = any(g in gtype for g in invalid)
    
    if test:
        
        raise TypeError('Only (MULTI)POLYGON geometry type allowed')
    
    if not gdf.crs == 'WGS 84':
         msg('Transforming shp to WGS 84')
         gdf = gdf.to_crs("EPSG:4326")
    
    if len(gdf) > 1:
        dVal = 1
        gdf['df'] = dVal
        gdf = gdf.dissolve(by = 'df')   
        
            
    # make the smallest request possible
    hull = gdf["geometry"].convex_hull
    
    # get the wkt representation of the convex hull
    wkt_str = hull.geometry.to_string(index = False, header = False)
    
    """Grab SSURGO geometry from user define AOI in wkt format
    
    :param str wkt: the wkt representation of the AOI extent\n
    :param boolen meta: get the column metadata returned in the JSON string, only suitable for arcgis features classes:
    :return: SSURGO spatial data in wkt format"""
    
    q = """~DeclareGeometry(@aoi)~

    select @aoi = geometry::STPolyFromText('""" + wkt_str + """' , 4326)

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
        qData = results.json()
        
        cols = qData.get('Table')[0]
        data = qData.get('Table')[1:]
    
        df = pd.DataFrame(data, columns = cols)
        geometry = df['geom'].map(shapely.wkt.loads)
        
        sda_gdf = gpd.GeoDataFrame(df, crs = "EPSG:4326", geometry = geometry)
    
        # assume it has to be clipped to original polygon
        result = gpd.clip(sda_gdf, gdf)
        
        return result
        
    
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
    :str name: provide a shapefile name. If None, SSURGO_WGS84.shp used
    :return: geopandas data frame epsg 4326"""
    
    import os, geopandas as gpd, pandas as pd
    pd.set_option('display.max_colwidth', None)
    
    
    err = None
    
    if not shp.endswith(".shp"):
        err = 'input '  + shp + ' does not appear to be a shapefile'
        raise TypeError(err)

    else:
        gdf = gpd.read_file(shp)
    
    
    soils = sdaCall(gdf)
    
    if soils is not None:
        
        soils.drop(['geom'], axis = 1, inplace=True)
    
        if export:
            
            dest = os.path.dirname(shp)
            
            if name is not None:
                if not name.endswith('.shp'):
                    name = name + '.shp'
                
            else:
                name = 'SSURGO_WGS84.shp'
        
            soils.to_file(os.path.join(dest, name))

        return soils
    

def gpkg(gpkg=str, layer=str, meta=False, export=False, name=None):
    
    """Grab SSURGO soil polygons using input geopackage layer for extent
    
    :str gpkg: path to geopackage\n
    :str layer: layer to use for extent\n
    :boolean meta: column metadata returned in JSON string, arcgis features classes only\n
    :boolean export: write results to source geopackage\n
    :str name: output layer name with, if None SSURGO_WGS8 used\n
    :return: geopandas data frame epsg 4326"""
    
    import geopandas as gpd, pandas as pd
    pd.set_option('display.max_colwidth', None)
    
    gdf = gpd.read_file(filename=gpkg, layer=layer)
    
    soils = sdaCall(gdf, meta=False)
    
    if export:
        
        soils.drop(['geom'], axis = 1, inplace=True)
        
        if name is None:
            name = "SSURGO_WGS84"  
    
        soils.to_file(gpkg, layer=name, driver="GPKG")
    
    return soils
    

def fgdb(gdb=str, layer=str, meta=False, export=False, name=None):
    
    """Grab SSURGO soil polygons using file geodatabse layer for extent
    
    :str gdb: path to file geodatabase\n
    :str layer: layer to use for extent\n
    :boolean meta: column metadata returned in JSON string, arcgis features classes only\n
    :boolean export: write a .shp result to parent directory of the file geodatabse\n
    :str name: output layer name with, if None SSURGO_WGS8 used\n
    :return: geopandas data frame epsg 4326"""
    
    import os, fiona, geopandas as gpd, pandas as pd
    pd.set_option('display.max_colwidth', None)
    
    # get layerindex
    lyrs = fiona.listlayers(gdb)
    idx = lyrs.index(layer)
   
    gdf = gpd.read_file(filename=gdb, layer=idx)
    
    soils = sdaCall(gdf)
    
    if export:
        
        dest = os.path.dirname(gdb)
        
        soils.drop(['geom'], axis = 1, inplace=True)
        
        if name is None:
            name = "SSURGO_WGS84"  
    
        soils.to_file(dest, layer=name)
    
    return soils
   
def gdf(geodf, meta=False):
    """Grab SSURGO soil polygons using existing GeoDataFrame

    :object geodf: GeoDataFrame\n
    :boolean meta: column metadata returned in JSON string, arcgis features classes only\n
    :return: geopandas data frame epsg 4326"""
    
    if str(type(geodf)) != "<class 'geopandas.geodataframe.GeoDataFrame'>":
        err = 'input does not appear to be a valid GeoDataFrame'
        raise TypeError(err)
    
    soils = sdaCall(geodf)
    
    return soils


    
        
    
    

    
        
    


