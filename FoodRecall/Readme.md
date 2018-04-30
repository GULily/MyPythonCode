## Food Recall Analysis

__Tableau Vis Link:__ https://public.tableau.com/profile/yi1507#!/vizhome/ANLY-501Project/RecalledFoodDataAnalysis

__Introduction__:
We scraped data from the Food and Drug Administration (FDA), which provides monitored food product recalls. 
According to FDA's own definition, "Class I" recall involves a health hazard situation in which there is a 
reasonable probability that eating the food will cause health problems or death. So in this project, 
we focus on "Class I" recalls. We also want to focus on recalled foods produced in US only, 
so we remove food recalls of other countries. We find that listeria monocytogenes, salmonella contamination, 
and undeclared allergens are the three most serious reasons for recalls.

This project answers the following questions:
* What are the most frequent words and topics in the FDA data?
* What's the relationship between different problem types and food types?
* Which states have the most serious recalls?

__Scrape.py:__ Scrape food recall records from FDA (https://open.fda.gov/food/enforcement/)
with queries 'classification:"Class+I"' and 'status:"Terminated"'. 
The results are in the files "ScrapeClassI.csv" and "ScrapeTerminated.csv".

__DataCleaning.ipynb:__ Clean and combine data sets.

__Topic_modeling.py:__ Use latent Dirichlet allocation (LDA) generate 6 topics. 



