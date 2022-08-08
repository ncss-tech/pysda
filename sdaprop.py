# -*- coding: utf-8 -*-
"""
Created on Thu May  6 14:20:56 2021

@author: Charles.Ferguson
"""

def numprops(show = False):
    
    """Numeric SSURGO propeties
    :bool show: set to True to print to screen.  Use shorthand notation for prop(erty) assignment.\n
    :return: dictionary of numeric SSURGO properties"""
    
    numdic = {'0.1 bar H2O - Rep Value': 'wtenthbar_r', '0.33 bar H2O - Rep Value': 'wthirdbar_r', '15 bar H2O - Rep Value': 'wfifteenbar_r', 'Available Water Capacity - Rep Value': 'awc_r', 'Bray 1 Phosphate - Rep Value': 'pbray1_r', 'Bulk Density 0.1 bar H2O - Rep Value': 'dbtenthbar_r', 'Bulk Density 0.33 bar H2O - Rep Value': 'dbthirdbar_r', 'Bulk Density 15 bar H2O - Rep Value': 'dbfifteenbar_r', 'Bulk Density oven dry - Rep Value': 'dbovendry_r', 'CaCO3 Clay - Rep Value': 'claysizedcarb_r', 'Calcium Carbonate - Rep Value': 'caco3_r', 'Cation Exchange Capcity - Rep Value': 'cec7_r', 'Coarse Sand - Rep Value': 'sandco_r', 'Coarse Silt - Rep Value': 'siltco_r', 'Effective Cation Exchange Capcity - Rep Value': 'ecec_r', 'Electrial Conductivity 1:5 by volume - Rep Value': 'ec15_r', 'Electrical Conductivity - Rep Value': 'ec_r', 'Exchangeable Sodium Percentage - Rep Value': 'esp_r', 'Extract Aluminum - Rep Value': 'extral_r', 'Extractable Acidity - Rep Value': 'extracid_r', 'Fine Sand - Rep Value': 'sandfine_r', 'Fine Silt - Rep Value': 'siltfine_r', 'Free Iron - Rep Value': 'freeiron_r', 'Gypsum - Rep Value': 'gypsum_r', 'Kf ': 'kffact', 'Ki ': 'kifact', 'Kr ': 'krfact', 'Kw ': 'kwfact', 'LEP - Rep Value': 'lep_r', 'Liquid Limit - Rep Value': 'll_r', 'Medium Sand - Rep Value': 'sandmed_r', 'Organic Matter - Rep Value': 'om_r', 'Oxalate Aluminum - Rep Value': 'aloxalate_r', 'Oxalate Iron - Rep Value': 'feoxalate_r', 'Oxalate Phosphate - Rep Value': 'poxalate_r', 'Plasticity Index - Rep Value': 'pi_r', 'Range Production - Favorable Year': 'rsprod_h', 'Range Production - Normal Year': 'rsprod_r', 'Range Production - Unfavorable Year': 'rsprod_l', 'Rock Fragments 3 - 10 cm - Rep Value': 'frag3to10_r', 'Rock Fragments > 10 cm - Rep Value': 'fraggt10_r', 'Rubbed Fiber % - Rep Value': 'fiberrubbedpct_r', 'Satiated H2O - Rep Value': 'wsatiated_r', 'Saturated Hydraulic Conductivity - Rep Value': 'ksat_r', 'Sodium Adsorption Ratio - Rep Value': 'sar_r', 'Sum of Bases - Rep Value': 'sumbases_r', 'Total Clay - Rep Value': 'claytotal_r', 'Total Phosphate - Rep Value': 'ptotal_r', 'Total Sand - Rep Value': 'sandtotal_r', 'Total Silt - Rep Value': 'silttotal_r', 'Unrubbed Fiber % - Rep Value': 'fiberunrubbedpct_r', 'Very Coarse Sand - Rep Value': 'sandvc_r', 'Very Fine Sand - Rep Value': 'sandvf_r', 'Water Soluble Phosphate - Rep Value': 'ph2osoluble_r', 'no. 10 sieve - Rep Value': 'sieveno10_r', 'no. 200 sieve - Rep Value': 'sieveno200_r', 'no. 4 sieve - Rep Value': 'sieveno4_r', 'no. 40 sieve - Rep Value': 'sieveno40_r'}
    
    if show:
        for k,v in numdic.items():
            print(k + ":::" + v)
        print('\n Use short hand version of property to supply to getprop function')
        
    return numdic

def catprops(show = False):
     
    """Categorical SSURGO propeties
    :bool show: set to True to print on screen.  Use shorthand notation for prop(erty) assignment.\n
    :return: dictionary of categorical SSURGO properties"""
    
    catdic = {'Corrosion of Concrete': 'corcon', 'Corrosion of Steel': 'corsteel', 'Drainage Class': 'drainagecl', 'Hydrologic Group': 'hydgrp', 'Taxonomic Class Name': 'taxclname', 'Taxonomic Order': 'taxorder', 'Taxonomic Particle Size' : 'taxpartsize' , 'Taxonomic Suborder': 'taxsuborder', 'Taxonomic Temperature Regime': 'taxtempregime', 'Wind Erodibility Group': 'weg', 'Wind Erodibility Index': 'wei', 't Factor': 'tfact'}
    
    if show:
        for k,v in catdic.items():
            print(k + " ::: " + v)
        print('\n Use short hand version of property to supply to getprop function')
    
    return catdic

def allprops(show = False):
    
    import collections
    
    """All SSURGO propeties
    :bool show: set to True to print on screen.  Use shorthand notation for prop(erty) assignment.\n
    :return: dictionary of call available SSURGO properties"""
     
    nprops = numprops()
    cprops = catprops()
    
    aprops = {**nprops, **cprops}
    saprops = collections.OrderedDict(sorted(aprops.items()))
    
    if show:
        for k,v in saprops.items():
            print(k + " ::: " + v)
        print('\n Use short hand version of property to supply to getprop function')
    
    return saprops
    
 

# (aProp, areaSym, aggMethod, tDep, bDep, mmC)
def getprop(df, column=str, prop=None, method=None,  top=None, bottom=None, minmax=None, prnt=None, meta=None):
    
    """Get SSURGO property from Soil Data Access.\n
    :df: pandas data frame\n
    :str column: pandas data frame column name\n
    :str prop: SSURGO property, use SSURGO column name, not alias\n
    :str method: aggregation method. \n
    :int top: top horizon depth range in centimeters\n
    :int bottom: bottom horizon depth range in centimeters\n
    :str minmax: set MIN or MAX for minmax method\n
    :bool prnt: set to True to print sql to screen\n
    :bool meta: unused (column metadata)
    :return: pandas data frame"""
    
    import json, requests, pandas as pd
    from json.decoder import JSONDecodeError
    from requests import exceptions

    pd.set_option('display.max_colwidth', None)

    warn = list()
    
    validmethod = ['wtd_avg', 'dom_comp_cat', 'dom_comp_num','dom_cond', 'minmax', 'muaggatt']
    
    if not method in validmethod:
        methodstr = ",".join(map("'{0}'".format, validmethod))
        err = 'Unknown aggregation method. Specify one of the following: ' + methodstr
        raise ValueError(err)
        
    nummethods = ['wtd_avg', 'dom_comp_num']
    catmethods = ['dom_comp_cat', 'dom_cond']
    minmaxmethod = ['minmax']
    # numerical validation
    if method in nummethods:
    
        try:
            
            props = numprops(show=False)
            
            if prop is None:
                err = 'Soil property is None.  You must select one.'
                raise TypeError(err)
            
            if top is None or bottom is None:
                err = 'Top and bottom parameters are required for the ' + method + ' aggregation method'
                raise TypeError(err)
            
            if not type(top) == int or not type(bottom) == int:
                err ='Top and bottom variables must be of type integer'
                raise TypeError(err)
           
            if not prop in props.values():
                err = 'the property: ' + prop + ' is not a valid choice for the ' + method + ' aggregation method'
                raise ValueError(err)
            
            if bottom < top:
                err = 'The value of bottom must be greater (deeper) than the value of top'
                raise AttributeError(err)
            
            if top > 200:
                warn.append('Depths greater than 200 cm are not recommended and may return NULL data')       
       
        except (TypeError, ValueError, AttributeError) as e:
            print(e)
            raise
   
    # categoriacal validation
    if method in catmethods:

        try:
            
            if prop is None:
                err = 'Soil property is None.  You must select one.'
                TypeError(err)
                
            props = catprops(show = False)
            if not prop in props.values():
                err = 'the property: ' + prop + ' is not a valid choice for the ' + method + ' aggregation method'
                raise ValueError(err)
        
        except (TypeError, ValueError) as e:
            print(e)
            raise
    
    if method in minmaxmethod:
        
        try:
            
            props = numprops(show=False)
            
            if prop is None:
                err = 'Soil property is None.  You must select one.'
                raise TypeError(err)
                
            if not prop in props.values():
                err = 'the property: ' + prop + ' is not a valid choice for the ' + method + ' aggregation method'
                raise ValueError(err)
        
            if minmax is None:
                err = 'min or max needs to be set in order to run the minmax aggregation method'
                raise ValueError(err)
            elif minmax.upper() not in ['MIN', 'MAX']:
                err = 'Unrecognized value for minmax.  Use MIN or MAX'
                raise ValueError(err)
                
        except (TypeError, ValueError, AttributeError) as e:
            print(e)
            raise

        
    if method == 'muaggatt': 
       if any(var is not None for var in [prop, top, bottom, minmax]):
           err = "The muaggatt method returns all fields (pre-aggregated properties) in this table. The parameters prop, top, bottom, minmax must equal None."
           raise TypeError(err)
                
    try:
    
        df[column] = df[column].astype('string')
        key_list = pd.Series(df[column].unique()).to_list()
        keys = ",".join(map("'{0}'".format, key_list))
        # return keylist   
        
        tDep = str(top)
        bDep = str(bottom)
        aProp = prop
        
        if not minmax == None:
            minmax = minmax.upper()
        
        if method == "dom_comp_cat":
            q = """--dominant component categorical
            SELECT areasymbol, musym, muname, mu.mukey  AS mukey, """ + aProp + """ AS """ + aProp +"""
            FROM legend  AS l
            INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey
            AND mu.mukey IN (""" + keys + """)
            INNER JOIN component AS c ON c.mukey = mu.mukey
            AND c.cokey =
            (SELECT TOP 1 c1.cokey FROM component AS c1
            INNER JOIN mapunit ON c.mukey=mapunit.mukey AND c1.mukey=mu.mukey ORDER BY c1.comppct_r DESC, c1.cokey)"""
        if method == "wtd_avg":
            q = """--weighted average
            SELECT areasymbol, musym, muname, mukey
            INTO #kitchensink
            FROM legend  AS lks
            INNER JOIN  mapunit AS muks ON muks.lkey = lks.lkey AND muks.mukey IN(""" + keys + """)
            SELECT mu1.mukey, cokey, comppct_r,
            SUM (comppct_r) over(partition by mu1.mukey ) AS SUM_COMP_PCT
            INTO #comp_temp
            FROM legend  AS l1
            INNER JOIN  mapunit AS mu1 ON mu1.lkey = l1.lkey AND mu1.mukey IN (""" + keys + """)
            INNER JOIN  component AS c1 ON c1.mukey = mu1.mukey AND majcompflag = 'Yes'
            SELECT cokey, SUM_COMP_PCT, CASE WHEN comppct_r = SUM_COMP_PCT THEN 1
            ELSE CAST (CAST (comppct_r AS  decimal (5,2)) / CAST (SUM_COMP_PCT AS decimal (5,2)) AS decimal (5,2)) END AS WEIGHTED_COMP_PCT
            INTO #comp_temp3
            FROM #comp_temp
            SELECT
            areasymbol, musym, muname, mu.mukey/1  AS MUKEY, c.cokey AS COKEY, ch.chkey/1 AS CHKEY, compname, hzname, hzdept_r, hzdepb_r, CASE WHEN hzdept_r <""" + tDep + """  THEN """ + tDep + """ ELSE hzdept_r END AS hzdept_r_ADJ,
            CASE WHEN hzdepb_r > """ + bDep + """  THEN """ + bDep + """ ELSE hzdepb_r END AS hzdepb_r_ADJ,
            CAST (CASE WHEN hzdepb_r > """ +bDep + """  THEN """ +bDep + """ ELSE hzdepb_r END - CASE WHEN hzdept_r <""" + tDep + """ THEN """ + tDep + """ ELSE hzdept_r END AS decimal (5,2)) AS thickness,
            comppct_r,
            CAST (SUM (CASE WHEN hzdepb_r > """ + bDep + """  THEN """ + bDep + """ ELSE hzdepb_r END - CASE WHEN hzdept_r <""" + tDep + """ THEN """ + tDep + """ ELSE hzdept_r END) over(partition by c.cokey) AS decimal (5,2)) AS sum_thickness,
            CAST (ISNULL (""" + aProp + """, 0) AS decimal (5,2))AS """ + aProp + """
            INTO #main
            FROM legend  AS l
            INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey AND mu.mukey IN (""" + keys + """)
            INNER JOIN  component AS c ON c.mukey = mu.mukey
            INNER JOIN chorizon AS ch ON ch.cokey=c.cokey AND hzname NOT LIKE '%O%'AND hzname NOT LIKE '%r%'
            AND hzdepb_r >""" + tDep + """ AND hzdept_r <""" + bDep + """
            INNER JOIN chtexturegrp AS cht ON ch.chkey=cht.chkey  WHERE cht.rvindicator = 'yes' AND  ch.hzdept_r IS NOT NULL
            AND texture NOT LIKE '%PM%' and texture NOT LIKE '%DOM' and texture NOT LIKE '%MPT%' and texture NOT LIKE '%MUCK' and texture NOT LIKE '%PEAT%' and texture NOT LIKE '%br%' and texture NOT LIKE '%wb%'
            ORDER BY areasymbol, musym, muname, mu.mukey, comppct_r DESC, cokey,  hzdept_r, hzdepb_r
            SELECT #main.areasymbol, #main.musym, #main.muname, #main.MUKEY,
            #main.COKEY, #main.CHKEY, #main.compname, hzname, hzdept_r, hzdepb_r, hzdept_r_ADJ, hzdepb_r_ADJ, thickness, sum_thickness, """ + aProp + """, comppct_r, SUM_COMP_PCT, WEIGHTED_COMP_PCT ,
            SUM((thickness/sum_thickness ) * """ + aProp + """ )over(partition by #main.COKEY)AS COMP_WEIGHTED_AVERAGE
            INTO #comp_temp2
            FROM #main
            INNER JOIN #comp_temp3 ON #comp_temp3.cokey=#main.cokey
            ORDER BY #main.areasymbol, #main.musym, #main.muname, #main.MUKEY, comppct_r DESC,  #main.COKEY,  hzdept_r, hzdepb_r
            SELECT #comp_temp2.MUKEY,#comp_temp2.COKEY, WEIGHTED_COMP_PCT * COMP_WEIGHTED_AVERAGE AS COMP_WEIGHTED_AVERAGE1
            INTO #last_step
            FROM #comp_temp2
            GROUP BY  #comp_temp2.MUKEY,#comp_temp2.COKEY, WEIGHTED_COMP_PCT, COMP_WEIGHTED_AVERAGE
            SELECT areasymbol, musym, muname,
            #kitchensink.mukey, #last_step.COKEY,
            CAST (SUM (COMP_WEIGHTED_AVERAGE1) over(partition by #kitchensink.mukey) as decimal(5,2))AS """ + aProp + """
            INTO #last_step2
            FROM #last_step
            RIGHT OUTER JOIN #kitchensink ON #kitchensink.mukey=#last_step.mukey
            GROUP BY #kitchensink.areasymbol, #kitchensink.musym, #kitchensink.muname, #kitchensink.mukey, COMP_WEIGHTED_AVERAGE1, #last_step.COKEY
            ORDER BY #kitchensink.areasymbol, #kitchensink.musym, #kitchensink.muname, #kitchensink.mukey
            SELECT #last_step2.areasymbol, #last_step2.musym, #last_step2.muname,
            #last_step2.mukey, #last_step2.""" + aProp + """
            FROM #last_step2
            LEFT OUTER JOIN #last_step ON #last_step.mukey=#last_step2.mukey
            GROUP BY #last_step2.areasymbol, #last_step2.musym, #last_step2.muname, #last_step2.mukey, #last_step2.""" + aProp + """
            ORDER BY #last_step2.areasymbol, #last_step2.musym, #last_step2.muname, #last_step2.mukey, #last_step2.""" + aProp
        if method == "minmax":
            q = """-- minimum maximum
            SELECT areasymbol, musym, muname, mu.mukey  AS mukey,
            (SELECT TOP 1 """ + minmax + """ (chm1.""" + aProp + """) FROM  component AS cm1
            INNER JOIN chorizon AS chm1 ON cm1.cokey = chm1.cokey AND cm1.cokey = c.cokey
            AND CASE WHEN chm1.hzname LIKE  '%O%' AND hzdept_r <10 THEN 2
            WHEN chm1.hzname LIKE  '%r%' THEN 2
            WHEN chm1.hzname LIKE  '%'  THEN  1 ELSE 1 END = 1
            ) AS """ + aProp + """
            FROM legend  AS l
            INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey AND mu.mukey IN (""" + keys + """)
            INNER JOIN  component AS c ON c.mukey = mu.mukey  AND c.cokey =
            (SELECT TOP 1 c1.cokey FROM component AS c1
            INNER JOIN mapunit ON c.mukey=mapunit.mukey AND c1.mukey=mu.mukey ORDER BY c1.comppct_r DESC, c1.cokey)"""
        if method == "dom_comp_num":
            q = """--dominant component numeric
            SELECT areasymbol, musym, muname, mukey
            INTO #kitchensink
            FROM legend  AS lks
            INNER JOIN  mapunit AS muks ON muks.lkey = lks.lkey AND muks.mukey  IN (""" + keys + """)
            SELECT mu1.mukey, cokey, comppct_r,
            SUM (comppct_r) over(partition by mu1.mukey ) AS SUM_COMP_PCT
            INTO #comp_temp
            FROM legend  AS l1
            INNER JOIN  mapunit AS mu1 ON mu1.lkey = l1.lkey AND mu1.mukey IN (""" + keys + """)
            INNER JOIN  component AS c1 ON c1.mukey = mu1.mukey AND majcompflag = 'Yes'
            AND c1.cokey =
            (SELECT TOP 1 c2.cokey FROM component AS c2
            INNER JOIN mapunit AS mm1 ON c2.mukey=mm1.mukey AND c2.mukey=mu1.mukey ORDER BY c2.comppct_r DESC, c2.cokey)
            SELECT cokey, SUM_COMP_PCT, CASE WHEN comppct_r = SUM_COMP_PCT THEN 1
            ELSE CAST (CAST (comppct_r AS  decimal (5,2)) / CAST (SUM_COMP_PCT AS decimal (5,2)) AS decimal (5,2)) END AS WEIGHTED_COMP_PCT
            INTO #comp_temp3
            FROM #comp_temp
            SELECT areasymbol, musym, muname, mu.mukey/1  AS MUKEY, c.cokey AS COKEY, ch.chkey/1 AS CHKEY, compname, hzname, hzdept_r, hzdepb_r, CASE WHEN hzdept_r < """ + tDep + """ THEN """ + tDep + """ ELSE hzdept_r END AS hzdept_r_ADJ,
            CASE WHEN hzdepb_r > """ + bDep + """  THEN """ + bDep + """ ELSE hzdepb_r END AS hzdepb_r_ADJ,
            CAST (CASE WHEN hzdepb_r > """ + bDep + """  THEN """ + bDep + """ ELSE hzdepb_r END - CASE WHEN hzdept_r <""" + tDep + """ THEN """ + tDep + """ ELSE hzdept_r END AS decimal (5,2)) AS thickness,
            comppct_r,
            CAST (SUM (CASE WHEN hzdepb_r > """ + bDep + """  THEN """ + bDep + """ ELSE hzdepb_r END - CASE WHEN hzdept_r <""" + tDep + """ THEN """ + tDep + """ ELSE hzdept_r END) over(partition by c.cokey) AS decimal (5,2)) AS sum_thickness,
            CAST (ISNULL (""" + aProp + """ , 0) AS decimal (5,2))AS """ + aProp + """
            INTO #main
            FROM legend  AS l
            INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey AND mu.mukey IN (""" + keys + """)
            INNER JOIN  component AS c ON c.mukey = mu.mukey
            INNER JOIN chorizon AS ch ON ch.cokey=c.cokey AND hzname NOT LIKE '%O%'AND hzname NOT LIKE '%r%'
            AND hzdepb_r >""" + tDep + """ AND hzdept_r <""" + bDep + """
            INNER JOIN chtexturegrp AS cht ON ch.chkey=cht.chkey  WHERE cht.rvindicator = 'yes' AND  ch.hzdept_r IS NOT NULL
            AND
            texture NOT LIKE '%PM%' and texture NOT LIKE '%DOM' and texture NOT LIKE '%MPT%' and texture NOT LIKE '%MUCK' and texture NOT LIKE '%PEAT%' and texture NOT LIKE '%br%' and texture NOT LIKE '%wb%'
            ORDER BY areasymbol, musym, muname, mu.mukey, comppct_r DESC, cokey,  hzdept_r, hzdepb_r
            SELECT #main.areasymbol, #main.musym, #main.muname, #main.MUKEY,
            #main.COKEY, #main.CHKEY, #main.compname, hzname, hzdept_r, hzdepb_r, hzdept_r_ADJ, hzdepb_r_ADJ, thickness, sum_thickness, """ + aProp + """ , comppct_r, SUM_COMP_PCT, WEIGHTED_COMP_PCT ,
            SUM((thickness/sum_thickness ) * """ + aProp + """)over(partition by #main.COKEY)AS COMP_WEIGHTED_AVERAGE
            INTO #comp_temp2
            FROM #main
            INNER JOIN #comp_temp3 ON #comp_temp3.cokey=#main.cokey
            ORDER BY #main.areasymbol, #main.musym, #main.muname, #main.MUKEY, comppct_r DESC,  #main.COKEY,  hzdept_r, hzdepb_r
            SELECT #comp_temp2.MUKEY,#comp_temp2.COKEY, WEIGHTED_COMP_PCT * COMP_WEIGHTED_AVERAGE AS COMP_WEIGHTED_AVERAGE1
            INTO #last_step
            FROM #comp_temp2
            GROUP BY  #comp_temp2.MUKEY,#comp_temp2.COKEY, WEIGHTED_COMP_PCT, COMP_WEIGHTED_AVERAGE
            SELECT areasymbol, musym, muname,
            #kitchensink.mukey, #last_step.COKEY,
            CAST (SUM (COMP_WEIGHTED_AVERAGE1) over(partition by #kitchensink.mukey) as decimal(5,2))AS """ + aProp + """
            INTO #last_step2
            FROM #last_step
            RIGHT OUTER JOIN #kitchensink ON #kitchensink.mukey=#last_step.mukey
            GROUP BY #kitchensink.areasymbol, #kitchensink.musym, #kitchensink.muname, #kitchensink.mukey, COMP_WEIGHTED_AVERAGE1, #last_step.COKEY
            ORDER BY #kitchensink.areasymbol, #kitchensink.musym, #kitchensink.muname, #kitchensink.mukey
            SELECT #last_step2.areasymbol, #last_step2.musym, #last_step2.muname,
            #last_step2.mukey, #last_step2.""" + aProp + """
            FROM #last_step2
            LEFT OUTER JOIN #last_step ON #last_step.mukey=#last_step2.mukey
            GROUP BY #last_step2.areasymbol, #last_step2.musym, #last_step2.muname, #last_step2.mukey, #last_step2.""" + aProp + """
            ORDER BY #last_step2.areasymbol, #last_step2.musym, #last_step2.muname, #last_step2.mukey, #last_step2.""" + aProp
        if method == 'muaggatt':
            q = """ --- map unit aggregae table
            SELECT musym,muname,mustatus,slopegraddcp,slopegradwta,brockdepmin,wtdepannmin,wtdepaprjunmin,
            flodfreqdcd,flodfreqmax,pondfreqprs,aws025wta,aws050wta,aws0100wta,aws0150wta,drclassdcd,drclasswettest,
            hydgrpdcd,iccdcd,iccdcdpct,niccdcd,niccdcdpct,engdwobdcd,engdwbdcd,engdwbll,engdwbml,
            engstafdcd,engstafll,engstafml,engsldcd,engsldcp,englrsdcd,engcmssdcd,engcmssmp,urbrecptdcd,
            urbrecptwta,forpehrtdcp,hydclprs,awmmfpwwta,mukey
            FROM muaggatt
            where mukey IN (""" + keys + """)"""            
        elif method == "dom_cond":
            q = """--dominant condition
            SELECT areasymbol, musym, muname, mu.mukey/1  AS mukey,
            (SELECT TOP 1 """ + aProp + """
            FROM mapunit
            INNER JOIN component ON component.mukey=mapunit.mukey
            AND mapunit.mukey = mu.mukey
            GROUP BY """ + aProp + """, comppct_r ORDER BY SUM(comppct_r) over(partition by """ + aProp + """) DESC) AS """ + aProp + """
            FROM legend  AS l
            INNER JOIN  mapunit AS mu ON mu.lkey = l.lkey AND  mu.mukey IN (""" + keys + """)
            INNER JOIN  component AS c ON c.mukey = mu.mukey
            AND c.cokey =
            (SELECT TOP 1 c1.cokey FROM component AS c1
            INNER JOIN mapunit ON c.mukey=mapunit.mukey AND c1.mukey=mu.mukey ORDER BY c1.comppct_r DESC, c1.cokey)
            GROUP BY areasymbol, musym, muname, mu.mukey, c.cokey,  compname, comppct_r
            ORDER BY areasymbol, musym, muname, mu.mukey, comppct_r DESC, c.cokey"""
        
        if prnt:
            print(q)
        
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
    
        property_result = pd.DataFrame(data, columns = cols)
        
        if len(warn) > 0:
            for w in warn:
                print('\n' + w + '\n')
        
        return property_result
    
    except (exceptions.InvalidURL, exceptions.HTTPError, exceptions.Timeout) as e:
        print(e)
        raise
        
    except JSONDecodeError as err:
        print('JSON Decode error: ' + err.msg)
        print('This usually happens when nothing is returned. Set prnt option to True and send the query through browser')
        raise
        
    except Exception as e:
        print('Unhandled error')
        print(e)
        raise
        