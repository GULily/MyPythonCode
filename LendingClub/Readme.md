## Summary

Author: Yi Li

__Data Source:__ The raw lending club loan data is downloaded from the website [Lending Club Statistics](https://www.lendingclub.com/info/download-data.action).

__Purpose:__ The purpose of this project is to predict whether a user is going to default on his or her loan. This is meaningful, because if we can predict and target these people, we can take actions earlier and reduce the default rate of a company.

__Method & Results:__ After lots of data exploration, data cleaning and feature engineering, I extracted 60+ features (110+ features after one-hot encoding for categorical features) from the original 150+ features. I defined the target "default" as any user whose loan status is past due (not "Current" and not "Fully Paid"). I split the cleaned dataset as a training dataset (70%) and a test dataset (30%).

I used two models: 

    (a) a logistic classifier with regularization (Lasso) to control multilinear problem 
    Training auc-score:99.4%, test auc-score: 99.4%,
    Training accuracy: 98.2%, test accuracy: 98.3% (threshold = 0.5). 
    
    Top features: 'pymnt_plan','last_credit_pull_d_since_issue','log_loan_amnt','disbursement_method','term','new_zip'(collapsed from the orginal feature 'zip_code'),'purpose','pub_rec_bankruptcies'
    
 
    (b) a random forest classifier
    Training auc-score:99.9%, test auc-score: 99.6%,
    Training accuracy: 98.8%, test accuracy: 98.4% (threshold = 0.5).

    Top features: 
    'next_pymnt_d_since_issue','last_pymnt_d_since_issue','out_prncp','last_pymnt_amnt','last_credit_pull_d_since_issue','total_rec_prncp','last_fico_range_low','total_rec_int','total_pymnt','collection_recovery_fee'
    

    
__Conclusion__: The results of model (b) is better than model (a). The top features achieved from two models are very different. *The logistic classifier prefers categorical features while the random forest classifier prefers numerical features.* They only share one common feature 'last_credit_pull_d_since_issue' (the number of days from last time pull credit since issue). Other important features including 'pymnt_plan' (which is "yes" or "no"), 'log_loan_amnt' (the log of loan amount), 'disbursement_method' (cash or directed pay), 'term'(36 or 60 months), 'next_pymnt_d_since_issue', 'last_pymnt_d_since_issue', 'out_prncp'(remaining outstanding principal for total amount funded), 'last_pymnt_amnt'.
    
