from add import *
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("User Analytics in the Telecommunication Industry")
st.write( """
        
        ##  The top 10 handsets used by the customers

         
         
         """)

top10= df[['Handset Type', 'IMSI']].groupby('Handset Type')
top10= top10['IMSI'].nunique().nlargest(10)
st.line_chart(top10)

#The top 5 handsets per top 3 handset manufacturer#Apple
st.write( """
        
        ## The top 5 handsets per top 3 handset manufacturer #Apple
         
         
         """)
y= df[df['Handset Manufacturer']=='Apple'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5)
st.line_chart(y)

st.write( """
        
        ## The top 5 handsets per top 3 handset manufacturer #Samsung
         
         
         """)
x=df[df['Handset Manufacturer']=='Samsung'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5)

st.line_chart(y)

st.write( """
        
        ## The top 5 handsets per top 3 handset manufacturer #Huawei
        
         """)
z=df[df['Handset Manufacturer']=='Huawei'].groupby(['Handset Type'])['IMSI'].nunique().nlargest(5)
st.line_chart(z)

st.write( """
       ## Aggregating per user the number of xDR session column
        
         """)

df_session_count = df.groupby(['MSISDN/Number'])['Bearer Id'].agg(['count'])
df_session_count

st.write( """
       ## Aggregating per user the Session duration column
        
         """)
# Aggregating per user the Session duration column
df_session_duration = df.groupby(['MSISDN/Number'])['Dur. (ms)'].agg(['sum'])
df_session_duration

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
st.write( """
       ## Aggregating per user the Total_Uploaded_Downloaded column
        
         """)

user_grp1 = df.groupby(['MSISDN/Number'])['Total_UL_DL'].agg(['min','max','mean','median','sum'])
user_grp1 

# # Aggregating per user the Social_Media_UL_DL column

# user_grp2 = df.groupby(['MSISDN/Number'])
# user_grp2['Social_Media_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# # Aggregating per user the Google_UL_DL column

# user_grp3 = df.groupby(['MSISDN/Number'])
# user_grp3['Google_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# # Aggregating per user the Email_UL_DL column

# user_grp4 = df.groupby(['MSISDN/Number'])
# user_grp4['Email_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

# # Aggregating per user the Youtube_UL_DL column

# user_grp5= df.groupby(['MSISDN/Number'])
# user_grp5['Youtube_UL_DL'].agg(['min','max','mean','median','sum']).head(10)

