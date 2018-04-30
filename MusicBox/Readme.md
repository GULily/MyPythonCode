## Summary

Author: Yi Li

__Data:__ Log data from some Chinese music box, the data including three different user activities: “play”, “search” and “download” from 2017-03-30 to 2017-05-12.

__Purpose:__ The purpose of this project is to predict churn rate to see how many users and what kind of users are going to churn. 

__Churn definition:__ if a user (uid) has one or more activities in the last 30 days (feature window) but has zero activity in the current 14 days (label window). 
    
    feature window: 2017-03-30 ~ 2017-04-28 days: 30
    label window: 2017-04-29 ~ 2017-05-12 days: 14

__Method & Results:__ After data exploration and data cleaning, I used Spark to do down sampling and extracted 10% users (uid) as the data are too larger. Then I used Spark to extract 20+ features during the feature window for each user (uid). These features including the frequency of __play, search, download__ music and the number of songs __played 80%__ (of their song length) in the __last 1, 3, 7, 14, 30 days__, and __device types__. 

I split the dataset into training:test as 7:3 and used two models to predict churn:

    (a) a logistic classifier with regularization to control multilinear problem 
    Training auc-score: 86%, test auc-score: 86%,
    Training accuracy: 78%, test accuracy: 78% (threshold = 0.5). 

    Top features: 
    device type, 
    the frequency of search music in the last 1, 3, 7, 14 days,
    the number of songs played 80% (of their song length) in the last 1, 3 days.

    (b) a random forest classifier
    Training auc-score: 91%, test auc-score: 90%,
    Training accuracy: 85%, test accuracy: 84% (threshold = 0.5).

    Top features: 
    the frequency of play music in the last 1, 3, 7, 14, 30 days, 
    the number of songs played 80% (of their song length) in the last 3, 7, 14, 30 days, 
    the frequency of search and download music in the last 30 days.


__Conclusions:__ The results of model (b) is better than model (a). The top features achieved from two models are very different. The logistic classifier prefers categorical features like __device types__ and features in recent days like __search__ and __played 80%__ in last 1 and 3 days. While the random forest classifier prefers numerical features more distance like __play, played 80%, searched__ in the 3, 7, 14, 30 days. 
