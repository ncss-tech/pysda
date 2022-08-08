# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:27:10 2022

@author: Charles.Ferguson
"""

def tabular(q, meta=False):
    
    """Submit your own custom Soil Data Access Query. If you get
    a JSONDecodeError: Expecting value, typically error will come
    from either too much data is being reuqested, or more likely
    there is a problem with you SQL syntax.  You can check your
    syntax here: https://sdmdataaccess.nrcs.usda.gov/Query.aspx
    
    :param q str: SQL query
    :return frame: pandas data frame"""
        
    import pandas as pd
    from pysda import caller
    
    resp, data = caller.sda(q=q, meta=False)
    
    if resp:
        
        table = data.get('Table')
        df = pd.DataFrame(data = table[1:], columns = table[0])
        return df
    else:
        #error should be thrown from caller
        pass
    