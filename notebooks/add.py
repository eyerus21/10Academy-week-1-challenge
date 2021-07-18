

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
df[df['Handset Manufacturer']=='Samsung'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5)
df[df['Handset Manufacturer']=='Huawei'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5)

# Aggregating per user the number of xDR session column
df_session_count = df.groupby(['MSISDN/Number'])['Bearer Id'].agg(['count'])
df_session_count.head(10)

# Aggregating per user the Session duration column
# Aggregating per user the Session duration column
df_session_duration = df.groupby(['MSISDN/Number'])['Dur. (ms)'].agg(['sum'])
df_session_duration.head(10)

#Total Data Uploaded and Downloaded¶
# adding two columns and forming a new column
def adding_columns(name,column1,column2):
    df[name] = df_clean[column1] + df_clean[column2]
    return df
adding_columns(name='Total_UL_DL',column1='Total UL (Bytes)',column2='Total DL (Bytes)')
adding_columns(name='Avg_RTT_UL_DL',column1='Avg RTT DL (ms)',column2='Avg RTT UL (ms)')
adding_columns(name='TCP_UL_DL_Retrans. Vol_(Bytes)',column1='TCP DL Retrans. Vol (Bytes)',column2='TCP UL Retrans. Vol (Bytes)')
adding_columns(name='Avg_ Bearer_TP DL_UL _(kbps)',column1='Avg Bearer TP DL (kbps)',column2='Avg Bearer TP UL (kbps)')
adding_columns(name='Social_Media_UL_DL',column1='Social Media DL (Bytes)',column2='Social Media UL (Bytes)')
adding_columns(name='Google_UL_DL',column1='Google DL (Bytes)',column2='Google UL (Bytes)')
adding_columns(name='Email_UL_DL',column1='Email DL (Bytes)',column2='Email DL (Bytes)')
adding_columns(name='Youtube_UL_DL',column1='Youtube DL (Bytes)',column2='Youtube DL (Bytes)')
adding_columns(name='Netflix_UL_DL',column1='Netflix DL (Bytes)',column2='Netflix UL (Bytes)')
adding_columns(name='Gaming_UL_DL',column1='Gaming DL (Bytes)',column2='Gaming UL (Bytes)')
adding_columns(name='Other_UL_DL',column1='Other DL (Bytes)',column2='Other UL (Bytes)')

# Aggregating per user the Total_UL_DL column

user_grp1 = df.groupby(['MSISDN/Number'])
user_grp1['Total_UL_DL'].agg(['min','max','mean','median','sum']).head(10)


# Aggregating per user the Social_Media_UL_DL column

user_grp2 = df.groupby(['MSISDN/Number'])
user_grp2['Social_Media_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# Aggregating per user the Google_UL_DL column

user_grp3 = df.groupby(['MSISDN/Number'])
user_grp3['Google_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# Aggregating per user the Email_UL_DL column

user_grp4 = df.groupby(['MSISDN/Number'])
user_grp4['Email_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# Aggregating per user the Youtube_UL_DL column

user_grp5= df.groupby(['MSISDN/Number'])
user_grp5['Youtube_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

