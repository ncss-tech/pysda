# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 08:08:39 2022

@author: Charles.Ferguson
"""

def availability(form=None, dest=None):

    """Download SSURGO Soil Survey Availability from Web Soil Survey.
    :param form str: select format, vaild types are 'pdf', 'jpg', 'shp'(shapefile). If None 'shp' will be downloaded
    :param dest str: destination directory.  If None specified download location is your current working directory
    :return: file object on disk"""

    import os, requests

    if form == 'pdf':
        pdf = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityMap.pdf'
        name = os.path.basename(pdf)
        r = requests.get(pdf)
    elif form == 'jpg':
        jpg = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityMap.jpg'
        name = os.path.basename(jpg)
        r = requests.get(jpg)
    elif form == 'shp' or form is None:
        shp = 'https://websoilsurvey.sc.egov.usda.gov/DataAvailability/SoilDataAvailabilityShapefile.zip'
        name = os.path.basename(shp)
        r = requests.get(shp)
    else:
        err = 'Unsupported format requested'
        raise RuntimeError(err)

    if dest is None:
        dest = os.getcwd()
    else:
        dest=dest

    try:
        open(os.path.join(dest,name), 'wb').write(r.content)
    except OSError as e:
        print(e)


def ssurgo(state=None, search=None):

    """Get the current available SSURGO downloads. Optionally you can filter to a state
    abbreviation like 'TX' or search for a soil survey area name (typically a county name) i.e.
    'lancaster'.  These options cannot be used together.

    :param state str: specify a state abbreviation such as 'NY'
    :param search str: specify a search term such as 'hamilton'
    :return  data frame: a pandas data frame"""
    
    import pandas as pd
    from pysda import caller
    

    valid = ['AK','AL','AR','AS','AZ','CA','CO','CT','DC','DE','FL','FM','GA',\
             'GU','HI','IA','ID','IL','IN','KS','KY','LA','MA','MD','ME','MH',\
            'MI','MN','MO','MP','MS','MT','NC','ND','NE','NH','NJ',\
            'NM','NV','NY','OH','OK','OR','PA','PR','PW','RI','SC',\
            'SD','TN','TX','UT','VA','VI','VT','WA','WI','WV','WY']

    query = """SELECT areasymbol, left(areasymbol, 2) as state, areaname, saverest
    FROM sacatalog"""

    if search is not None and state is not None :
            err = 'state and search parameters cannot be run together. provide only 1'
            raise RuntimeWarning(err)

    elif not state is None and len(state) == 2 and state in valid:
        query = query + """ WHERE left(areasymbol, 2) = '""" + state + """'"""

    elif search is not None:
        query = query + """ WHERE UPPER(areaname) LIKE '%""" + search + """%'"""

    elif state is not None and state not in valid:
        choice = ",".join(map('{0}'.format, valid))
        err = 'Unknown state abbreviation, select 1 from: ' + choice
        raise ValueError(err)

    resp, value = caller.sda(query,False)

    if resp:

        columns = value.get('Table')[0]
        data = value.get('Table')[1:]
        # print(columns)
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

def download(frame, dest=None, unpack=None, rename=None):

    """Download SSURGO data sets from Web Soil Survey (WSS) using URLs.
    :param frame: preferrably this is a pandas data frame, an iterable containing WSS URLs is also valid
    :param dest str: specifiy a download directory.  If None, the download will go to os.getcwd()
    :param unpack boolean: unpack the zip file in dest
    :param rename boolean: rename an upacked download dir to traditional SSURGO conventions i.e. soil_nc001"""


    if not unpack:
        if rename:
            err = 'Yan cannot rename if you do not unpack first'
            raise RuntimeError(err)

    import os, requests, zipfile

    try:

        import pandas as pd

        if isinstance(frame, pd.DataFrame):

            df = pd.DataFrame(frame)
            URLS = df['URL'].to_list()
        
        else:
            
            try:
                iter(frame)
                URLS = frame
            
            except TypeError as e:
                raise(e)
    
    except:
        err = 'Download URLs are not iterable or invalid'
        raise TypeError(err)

    prefix = 'https://websoilsurvey.sc.egov.usda.gov/DSD/Download/Cache/SSA/wss_SSA_'
    idx = len(prefix)

    if dest is None:
        dest = os.getcwd()

    for url in URLS:

        if url.startswith(prefix):

            try:

                print('Attempting download for ' + url[idx:idx+5])
                r = requests.get(url)

            except requests.exceptions.RequestException as e:
                print('Problem downloading ' + url[idx:idx+5])
                print(e)

            except Exception as e:
                print(e)

            try:

                open(os.path.join(dest,(os.path.basename(url))), 'wb').write(r.content)

                if unpack:
                    with zipfile.ZipFile(os.path.join(dest,os.path.basename(url)), 'r') as z:
                        z.extractall(dest)

                        if rename:
                            base = os.path.basename(url)
                            area = base[8:13]
                            org = os.path.join(dest, area)
                            os.rename(org, os.path.join(dest, 'soil_' + area.lower()))

            except OSError as e:
                print(e)

        else:
            print(url + ' does not appear to be a valid url')

def outofcycle():
     """SSURGO data sets are updated annually around October 1.  Throughout the year
     it is possible a survey area is uploaded after this date.  This function identifies
     these survey areas which will help you determine if your local data set(s) need updating.

     :return data frame: pandas data frame"""
     
     import pandas as pd
     from pysda import caller
     
     q = """select left(areasymbol, 2) as state, areasymbol, saverest
     from sacatalog
     where saverest > '10-01-2021'
     ORDER BY areasymbol, saverest"""

     resp, data = caller.sda(q=q, meta=False)

     table = data.get('Table')

     df = pd.DataFrame(data = table[2:], columns = table[0])

     return df

















