import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
#The object returned by load_breast_cancer() is a scikit-learn Bunch object, which is similar to a dictionary.
#print(cancer.DESCR) # Print the data set description

cancer.keys()
#print('cancer feature names=', cancer['feature_names'])
#print('************************************')


cancer_df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
cancer_df['target']=cancer['target']
cancer_df.head()
print(cancer_df.columns)
print(type(cancer.feature_names))

#Question 2
benign=0
malignant=0
#print(len(cancer_df['target']))
for i in range(len(cancer_df['target'])):
    #print(type(cancer_df['target'][i]))
    if cancer_df['target'][i]==1:
        benign = benign+1
    elif cancer_df['target'][i]==0:
        malignant = malignant+1
    else: print('error')
#print(cnt)
target=pd.Series([malignant, benign],index=['malignant','benign'])
print(target)

#Question3
