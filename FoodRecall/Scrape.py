# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 10:13:36 2016

@author: Yi
"""

## https://open.fda.gov/food/enforcement/

import json
import urllib
from urllib.request import urlopen

    
## Scrape food recall data with classification: Class I 
## For this scraping, we exclude the attribute of "termination_date", because if one record's status is not terminated, it doesn't have "termination_date" attribute.
## And if we add the attribute of "termination_date", the output results will be wrong.    
def ScrapeClassI():
    ## write header with "w"
    with open("ScrapeClassI.csv", "w", encoding="utf-8") as f:
           f.write('event_id' + "," + 'recall_number' + "," + 'classification' + "," + 'product_type' + "," + 'status' + "," 
                    + 'postal_code' + "," + 'country' + "," + 'state' + "," + 'city' + "," + "distribution_pattern" + "," + 'recalling_firm' + ","
                    + 'initial_firm_notification' + "," + 'recall_initiation_date' + "," + 'report_date' + "," ##+ 'termination_date' + ","
                    + 'center_classification_date' + "," + 'reason_for_recall' + "," + 'product_description' + "," + 'code_info' + ","
                    + 'voluntary_mandated' + "\n")
               
    ## https://api.fda.gov/drug/event.json?api_key=yourAPIKeyHere&search=...
    baseURL="https://api.fda.gov/food/enforcement.json?"
    ## Post: status='Terminated&status:""'
    search='classification:"Class+I"'
    limit=100 # Limit cannot exceed 100 results for search requests. Use the skip param to get additional results.
    skip = 0
    while (skip < 6500):
        myURL=baseURL + urllib.parse.urlencode({
            'search':search,
            'limit': limit,
            'skip':skip,
            'api_key':'gBvl5QLZpRtnoIRgGqHb9U4Es1rOfyWOLOpIqdn6'
        })
        #print(myURL)
        response=urlopen(myURL).read().decode('utf-8')
        JSONresp=json.loads(response)
        resp = JSONresp['results']
        #print(resp)
        for list in resp:
            ID = list['event_id']
            ReNum = list['recall_number']
            Class = list['classification']
            ProdType = list['product_type']
            Status = list['status']
            PCode = list['postal_code']
            Country = list['country']
            State = list['state']
            City = list['city']
            DisPattern = list['distribution_pattern'].lower()
            ReFirm = list['recalling_firm'].lower()
            IFN = list['initial_firm_notification'].lower()
            RID = list['recall_initiation_date']
            RD = list['report_date']
#            try:
#                TD = list['termination_date']
#            except:
#                pass
            CCD = list['center_classification_date']
            Recall = list['reason_for_recall'].lower()
            ProdDescrip = list['product_description'].lower()
            CodeInfo = list['code_info'].lower()
            VM = list['voluntary_mandated']
        
            with open("ScrapeClassI.csv", "a", encoding="utf-8") as f:
                f.write(ID + ","  +  ReNum + ","  +  Class + "," + ProdType + "," + Status + ","
                    + PCode + "," + Country + "," + State + "," + City + "," + DisPattern.replace(',','').replace('.','') + "," 
                    + ReFirm.replace(',','').replace('.','') + "," + IFN.replace(',','').replace('.','') + "," + RID + "," + RD + "," ##+ TD + "," 
                    + CCD + "," + Recall.replace(',','').replace('.','') + "," + CodeInfo.replace(',','').replace('.','') + ","
                    + ProdDescrip.replace(',','').replace('.','') + "," + VM + "\n") 
        skip = skip + 100
        print(skip)  
ScrapeClassI()

## Scrape food recall data which have termination date. 
## If one record's status is not terminated, it doesn't have "termination_date" attribute, thus it effects all scraping data.
## During our scraping, we find some times even one record's status is terminated, it may still doesn't have "termination_date" attribute.
## In this case, the output result will stop where it should not, and we need skip the record manully by change the value of "skip".
def ScrapeTerminated():
    ## write header with "w"
    with open("ScrapeTerminated.csv", "w", encoding="utf-8") as f:
            f.write('event_id' + "," + 'recall_number' + "," + 'classification' + "," + 'product_type' + "," + 'status' + "," 
                    + 'postal_code' + "," + 'country' + "," + 'state' + "," + 'city' + "," + "distribution_pattern" + "," + 'recalling_firm' + ","
                    + 'initial_firm_notification' + "," + 'recall_initiation_date' + "," + 'report_date' + ","
                    + 'termination_date' + "," + 'center_classification_date' + "," + 'reason_for_recall' + "," + 'product_description' + "," + 'code_info' + ","
                    + 'voluntary_mandated' + "\n")
               
    ##https://api.fda.gov/drug/event.json?api_key=yourAPIKeyHere&search=...
    baseURL="https://api.fda.gov/food/enforcement.json?"
    ## Post: status='Terminated&status:""'
    search='status:"Terminated"'
    limit=100 ## Limit cannot exceed 100 results for search requests. Use the skip param to get additional results.
    skip = 0
    while (skip < 8000):
        myURL=baseURL + urllib.parse.urlencode({
            'search':search,
            'limit': limit,
            'skip':skip,
            'api_key':'gBvl5QLZpRtnoIRgGqHb9U4Es1rOfyWOLOpIqdn6'
        })
        #print(myURL)
        response=urlopen(myURL).read().decode('utf-8')
        JSONresp=json.loads(response)
        resp = JSONresp['results']
        #print(resp)
        for list in resp:
            ID = list['event_id']
            ReNum = list['recall_number']
            Class = list['classification']
            ProdType = list['product_type']
            Status = list['status']
            PCode = list['postal_code']
            Country = list['country']
            State = list['state']
            City = list['city']
            DisPattern = list['distribution_pattern'].lower()
            ReFirm = list['recalling_firm'].lower()
            IFN = list['initial_firm_notification'].lower()
            RID = list['recall_initiation_date']
            RD = list['report_date']
            try:
                TD = list['termination_date']
            except:
                pass
            CCD = list['center_classification_date']
            Recall = list['reason_for_recall'].lower()
            ProdDescrip = list['product_description'].lower()
            CodeInfo = list['code_info'].lower()
            VM = list['voluntary_mandated']
        
            with open("ScrapeTerminated.csv", "a", encoding="utf-8") as f:
                f.write(ID + ","  +  ReNum + ","  +  Class + "," + ProdType + "," + Status + ","
                    + PCode + "," + Country + "," + State + "," + City + "," + DisPattern.replace(',','').replace('.','') + "," 
                    + ReFirm.replace(',','').replace('.','') + "," + IFN.replace(',','').replace('.','') + "," + RID + "," + RD +"," + TD + "," 
                    + CCD + "," + Recall.replace(',','').replace('.','') + "," + CodeInfo.replace(',','').replace('.','') + ","
                    + ProdDescrip.replace(',','').replace('.','') + "," + VM + "\n") 
        skip = skip + 100
        print(skip)  
ScrapeTerminated()

