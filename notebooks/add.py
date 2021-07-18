

import statsmodels.api as sm
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set()
from sklearn.preprocessing import StandardScaler,normalize
from sklearn.cluster import KMeans
import scipy.spatial.distance as sdist
import sklearn.cluster as cluster
import math

import warnings
warnings.filterwarnings('ignore')
import statsmodels.api as sm
warnings.filterwarnings('ignore')


pd.set_option('max_column',None)
db= pd.read_csv('/home/eyerusalem/Documents/10Academy-week-1-challenge/data/Week1_challenge_data_source(CSV).csv', na_values= ['?', None])
db.head()

def percent_missing(df):
    totalcells= np.product(df.shape)
   
    missingCount= df.isnull().sum()
    #print(missingCount)
    totalMissing= missingCount.sum()
    print("The telecom data contains", round(((totalMissing/totalcells)*100),3),"%" ,"missing values")
percent_missing(db['Nb of sec with 6250B < Vol UL < 37500B'])
    
    
df_clean= db.drop(['Nb of sec with 125000B < Vol DL' ,'Nb of sec with 1250B < Vol UL < 6250B', 'Nb of sec with 31250B < Vol DL < 125000B','Nb of sec with 37500B < Vol UL' ,'Nb of sec with 6250B < Vol DL < 31250B', 'Nb of sec with 6250B < Vol UL < 37500B','Nb of sec with 6250B < Vol UL < 37500B'], axis=1)    
df = df_clean[~np.isnan(db['Bearer Id'])]
df = df_clean[~np.isnan(db['MSISDN/Number'])]
    
df['Bearer Id'] = df['Bearer Id'].apply(lambda x: '{:.0f}'.format(x))
df['Bearer Id'] = df['Bearer Id'].astype('str')

df["Start"]=pd.to_datetime(df["Start"], format='%m/%d/%Y %H:%M', errors='coerce')
df["End"]=pd.to_datetime(df["End"], format='%m/%d/%Y %H:%M', errors='coerce')

df['MSISDN/Number'] = df['MSISDN/Number'].apply(lambda x: '{:.0f}'.format(x))
df['MSISDN/Number'] = df['MSISDN/Number'].astype('str')

df['IMSI'] = df['IMSI'].apply(lambda x: '{:.0f}'.format(x))
df['IMSI'] = df['IMSI'].astype('str')

df['IMEI'] = df['IMEI'].apply(lambda x: '{:.0f}'.format(x))
df['IMEI'] = df['IMEI'].astype('str')

df['Handset Manufacturer'] = df['Handset Manufacturer'].astype('str')
df['Last Location Name'] = df['Last Location Name'].astype('str')

top10= df[['Handset Type', 'IMSI']].groupby('Handset Type')
top10= top10['IMSI'].nunique().nlargest(10)
y=df[['Handset Manufacturer','IMSI']].groupby(['Handset Manufacturer'])['IMSI'].nunique().nlargest(3)
#Apple
df[df['Handset Manufacturer']=='Apple'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5).plot(kind='barh')