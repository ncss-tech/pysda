# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:20:56 2021

@author: Charles.Ferguson
"""
def interps():
    """:run this for a list of interpretations:"""
    
    interps = ['AGR - Pesticide Loss Potential-Leaching', 'AGR - Pesticide Loss Potential-Soil Surface Runoff', 'AWM - Irrigation Disposal of Wastewater', 'AWM - Land Application of Municipal Sewage Sludge', 'AWM - Manure and Food Processing Waste', 'AWM - Overland Flow Process Treatment of Wastewater', 'AWM - Rapid Infiltration Disposal of Wastewater', 'AWM - Slow Rate Process Treatment of Wastewater', 'DHS - Catastrophic Mortality, Large Animal Disposal, Pit', 'DHS - Catastrophic Mortality, Large Animal Disposal, Trench', 'DHS - Potential for Radioactive Bioaccumulation', 'DHS - Potential for Radioactive Sequestration', 'DHS - Rubble and Debris Disposal, Large-Scale Event', 'DHS - Site for Composting Facility - Subsurface', 'DHS - Site for Composting Facility - Surface', 'DHS - Suitability for Clay Liner Material', 'DHS - Suitability for Composting Medium and Final Cover', 'ENG - Construction Materials{:} Gravel Source', 'ENG - Construction Materials{:} Reclamation', 'ENG - Construction Materials{:} Roadfill', 'ENG - Construction Materials{:} Sand Source', 'ENG - Construction Materials{:} Topsoil', 'ENG - Daily Cover for Landfill', 'ENG - Dwellings W/O Basements', 'ENG - Dwellings With Basements', 'ENG - Lawn, Landscape, Golf Fairway', 'ENG - Local Roads and Streets', 'ENG - Sanitary Landfill (Area)', 'ENG - Sanitary Landfill (Trench)', 'ENG - Septic Tank Absorption Fields', 'ENG - Sewage Lagoons', 'ENG - Shallow Excavations', 'ENG - Small Commercial Building', 'ENG - Unpaved Local Roads and Streets', 'FOR - Construction Limitations for Haul Roads/Log Landings', 'FOR - Hand Planting Suitability', 'FOR - Harvest Equipment Operability', 'FOR - Log Landing Suitability', 'FOR - Mechanical Planting Suitability', 'FOR - Mechanical Site Preparation (Deep)', 'FOR - Mechanical Site Preparation (Surface)', 'FOR - Potential Erosion Hazard (Off-Road/Off-Trail)', 'FOR - Potential Erosion Hazard (Road/Trail)', 'FOR - Potential Fire Damage Hazard', 'FOR - Potential Seedling Mortality', 'FOR - Road Suitability (Natural Surface)', 'FOR - Soil Rutting Hazard', 'GRL - Fencing, Post Depth =<24 inches', 'GRL - Fencing, Post Depth =<36 inches', 'Ground Penetrating Radar Penetration', 'MIL - Bivouac Areas (DOD)', 'MIL - Excavations Crew-Served Weapon Fighting Position (DOD)', 'MIL - Excavations for Individual Fighting Position (DOD)', 'MIL - Excavations for Vehicle Fighting Position (DOD)', 'MIL - Helicopter Landing Zones (DOD)', 'MIL - Trafficability Veh. Type 1 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 1 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 1 dry season (DOD)', 'MIL - Trafficability Veh. Type 2 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 2 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 2 dry season (DOD)', 'MIL - Trafficability Veh. Type 3 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 3 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 3 dry season (DOD)', 'MIL - Trafficability Veh. Type 4 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 4 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 4 dry season (DOD)', 'MIL - Trafficability Veh. Type 5 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 5 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 5 dry season (DOD)', 'MIL - Trafficability Veh. Type 6 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 6 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 6 dry season (DOD)', 'MIL - Trafficability Veh. Type 7 1-pass wet season (DOD)', 'MIL - Trafficability Veh. Type 7 50-passes wet season (DOD)', 'MIL - Trafficability Veh. Type 7 dry season (DOD)', 'NCCPI - National Commodity Crop Productivity Index (Ver 2.0)', 'URB/REC - Camp Areas', 'URB/REC - Off-Road Motorcycle Trails', 'URB/REC - Paths and Trails', 'URB/REC - Picnic Areas', 'URB/REC - Playgrounds', 'WMS - Embankments, Dikes, and Levees', 'WMS - Excavated Ponds (Aquifer-fed)', 'WMS - Irrigation, General', 'WMS - Irrigation, Micro (above ground)', 'WMS - Irrigation, Micro (subsurface drip)', 'WMS - Irrigation, Micro (subsurface drip) edited', 'WMS - Irrigation, Sprinkler (close spaced outlet drops)', 'WMS - Irrigation, Sprinkler (general)', 'WMS - Irrigation, Surface (graded)', 'WMS - Irrigation, Surface (level)', 'WMS - Pond Reservoir Area', 'WMS - Subsurface Water Management, Outflow Quality', 'WMS - Subsurface Water Management, System Installation', 'WMS - Subsurface Water Management, System Performance', 'WMS - Surface Water Management, System']
    for i in interps:
        print(i)
        
def interpDC(interp=str, kl=list):
    
    keys = ",".join(map("'{0}'".format, kl))
     
    q = """SELECT areasymbol, musym, muname, mu.mukey  AS MUKEY,
(SELECT interphr FROM component INNER JOIN cointerp ON component.cokey = cointerp.cokey AND component.cokey = c.cokey AND ruledepth = 0 AND mrulename LIKE '""" + interp + """') as rating,
(SELECT interphrc FROM component INNER JOIN cointerp ON component.cokey = cointerp.cokey AND component.cokey = c.cokey AND ruledepth = 0 AND mrulename LIKE '""" + interp + """') as class,
(SELECT DISTINCT SUBSTRING(  (  SELECT ( '; ' + interphrc)
FROM mapunit
INNER JOIN component ON component.mukey=mapunit.mukey AND compkind != 'miscellaneous area' AND component.cokey=c.cokey
INNER JOIN cointerp ON component.cokey = cointerp.cokey AND mapunit.mukey = mu.mukey
AND ruledepth != 0 AND interphrc NOT LIKE 'Not%' AND mrulename LIKE '""" + interp + """' GROUP BY interphrc, interphr
ORDER BY interphr DESC, interphrc
FOR XML PATH('') ), 3, 1000) )as reason
FROM legend  AS l
INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey AND mu.mukey IN (""" + keys + """)
INNER JOIN  component AS c ON c.mukey = mu.mukey  AND c.cokey = (SELECT TOP 1 c1.cokey FROM component AS c1
INNER JOIN mapunit ON c.mukey=mapunit.mukey AND c1.mukey=mu.mukey ORDER BY c1.comppct_r DESC, c1.cokey)"""

    return q
        
def sdaCall(query, meta=False):
    try:
        theURL = "https://sdmdataaccess.nrcs.usda.gov"
        theURL = theURL + "/Tabular/SDMTabularService/post.rest"
        
        rDic = {}
        
        if meta:
            rDic["format"] = "JSON+COLUMNNAME+METADATA"
        else:
            rDic["format"] = "JSON+COLUMNNAME"
        
        rDic["query"] = query
        rData = json.dumps(rDic)
        
        results = requests.post(data=rData, url=theURL)
        # print('results are next')
        # print(results)
        qData = results.json()
        print(qData)
        cols = qData.get('Table')[0]
        data = qData.get('Table')[1:]
    
        df = pd.DataFrame(data, columns = cols)
        
        return df
        
    
    except:
        print('dunno')
    

    
    


import json, requests, pandas as pd, geopandas as gpd

