def sda(q=str, meta=False):
    """accessing Soil Data Access POST REST API
       
       :str q: query sent to doil data access
       :bool meta: instructions for returning column information
       :return: python dictionary"""
    
    import requests, json
    from json.decoder import JSONDecodeError
    
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
        
        data = results.json()
            
        # cols = qData.get('Table')[0]
        # data = qData.get('Table')[1:]
            
        return True, data
        
    except JSONDecodeError as e:
        msg = e
        print(msg)
        return False, msg
    
    except requests.exceptions.RequestException as e:
        # msg = e.msg
        # print('Requests error: ' + msg)
        return False, e
    
    except Exception as e:
        msg = 'Unhadled error in Soil Data Access caller ' + e
        print(msg)
        return False, msg