## Food Recall Analysis

__Introduction__:
We scraped data from the Food and Drug Administration (FDA, https://open.fda.gov/food/enforcement/), which provides monitored food product recalls. 
According to FDA's own definition, "Class I" recall involves a health hazard situation in which there is a 
reasonable probability that eating the food will cause health problems or death. So in this project, 
we focus on "Class I" recalls. We also want to focus on recalled foods produced in US only, 
so we remove food recalls of other countries. We find that listeria monocytogenes, salmonella contamination, 
and undeclared allergens are the three most serious reasons for recalls.

This project answers the following questions:
* What are the most frequent words and topics in the FDA data?
* What's the relationship between different problem types and food types?
* Which states have the most serious recalls?

<p align="center">
  <img src="https://github.com/GULily/Projects/blob/master/FoodRecall/Wordcloud.png" width="300"/>
</p>

<p align="center">
  <img src="https://github.com/GULily/Projects/blob/master/FoodRecall/TopicModeling.png" width="400"/>
  <img src="https://github.com/GULily/Projects/blob/master/FoodRecall/TopicModeling2.png" width="400"/>
</p>

Here are the six topics we created. The words in red represent the causes; the words in orange represent the kinds of food or product; the words in blue represent the recalling firms or recalling firms' location (state or city). Among the six topics, five of them mention "listeria monocytogenes", and two of them mention "salmonella". Companies like Dole Fresh Vegetables, Blue Bell Creameries, Garden-Fresh Foods, and Sunopta Food and Grain seem to be the main recalling firms.

<p align="center">
  <img src="https://github.com/GULily/Projects/blob/master/FoodRecall/Table.png" width="400"/>
  <img src="https://github.com/GULily/Projects/blob/master/FoodRecall/Map.png" width="450"/>
</p>

__Tableau Vis Link:__ https://public.tableau.com/profile/yi1507#!/vizhome/ANLY-501Project/RecalledFoodDataAnalysis

Note: For the Map of Problem Types, we did not normalize the data based on the population of food companies of each state.



