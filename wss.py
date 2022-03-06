# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:08:39 2022

@author: Charles.Ferguson
"""

def avail(form=str, dest=None):
    
    """Download SSURGO Soil Survey Availability from Web Soil Survey.
    :param form str: select format, vaild types are pdf, jpg, shp(shapefile)
    :param dest str: destination directory"""
    
    import os, requests
    
    pdf = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityMap.pdf'
    jpg = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityMap.jpg'
    shp = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityShapefile.zip'
    
    r = requests.get(pdf)
    
    if dest is None:
        dest = os.getcwd()
    open(os.path.join(dest,(os.path.basename(pdf))), 'wb').write(r.content)
    

def ssainfo(state=None):
    
    import caller, pandas as pd
    
    valid = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','FM','GA',\
             'GU','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MH',\
            'MI','MN','MO','MP','MS','MT','MX','NC','ND','NE','NH','NJ',\
            'NM','NV','NY','OH','OK','OR','PA','PR','PW','RI','SC',\
            'SD','TN','TX','US','UT','VA','VI','VT','WA','WI','WV','WY']
    
    if not state is None and len(state) != 2 or state not in valid:
        err = 'Unknown state provided'
        raise AttributeError(err)
    
    if state is None:
       
        query = """SELECT areasymbol, left(areasymbol, 2) as state, areaname, saverest
        FROM sacatalog"""
    
    else:
        
        query = """SELECT areasymbol, left(areasymbol, 2) as state, areaname, saverest
        FROM sacatalog
        WHERE left(areasymbol, 2) = '""" + state + """'"""
    
    resp, value = caller.sda(query,False)
    
    if resp:
        
        columns = value.get('Table')[0]
        data = value.get('Table')[1:]
        print(columns)
        df = pd.DataFrame(data=data, columns=columns)
        
        ver = df['saverest'].to_list()
        date = list()
        for i in ver:
            idx = i.find(" ")
            space = i[:idx]
            items = space.split('/')
            month = items[0]
            if len(month) == 1:
                month = '0' + month
            
            day = items[1]
            if len(day) == 1:
                day = '0'+ day
            
            year = items[2]
            
            upload = year + '-' + month + '-' + day
            date.append(upload)

        df['date'] = date
        
        states = df['state'].to_list()
        templates = ['AK', 'CT', 'FL', 'GA', 'HI', 'IA', 'ID', 'IN', 'ME', 'MI', 'MN', 'MT',\
                     'NC', 'NE', 'NJ', 'OH', 'OR', 'PA', 'SD', 'UT', 'VT', 'WA', 'WI', 'WV',\
                    'WY', 'FM']
        dbState = list()

        for s in states:
            if s in templates:
                dbState.append('_soildb_' + s + '_2003_')
            else:
                dbState.append('_soildb_US_2003_')

        df['db'] = dbState

        prefix = 'https://websoilsurvey.sc.egov.usda.gov/DSD/Download/Cache/SSA/wss_SSA_'
        df['URL'] = prefix + df['areasymbol'] + df['db'] + "[" + df['date'] +'].zip'
        df.drop(['date', 'db'], axis = 1, inplace=True)
        
        return df
        
    else:
        
        # didn't get the 
        # areasymbols correctly
        print(value)
  
def soildownload(frame, column='URL', dest=str):
    
    import os, requests, pandas as pd
    
    df = pd.DataFrame(frame)
    
    areas = df[column].to_list()
    prefix = prefix = 'https://websoilsurvey.sc.egov.usda.gov/DSD/Download/Cache/SSA/wss_SSA_'
    idx = len(prefix)
    
    if dest is None:
        dest = os.getcwd()
    
    for area in areas:
        print(area)
        print('Downloading ' + area[idx:idx+5])
        r = requests.get(area)
        open(os.path.join(dest,(os.path.basename(area))), 'wb').write(r.content)
        
        
    
    

    
    
    
    




