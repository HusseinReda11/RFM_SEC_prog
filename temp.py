import pandas as pd
import datetime as dt 
import matplotlib.pyplot as plt
path_file="D:\\AssRFM\\250000Sales Records.csv"
data= pd.read_csv(path_file)
data.info() 

df=pd.DataFrame(data)
df


df.dropna(subset="Customer ID")
df.drop_duplicates(inplace=True)
df.shape

filter_df = df[["Customer ID", "Order ID", "Total Revenue", "Order Date"]]
# Ensure 'Order Date' is in datetime format
filter_df['Order Date'] = pd.to_datetime(filter_df['Order Date'])
now_date=dt.datetime.now()
now_date

rfm=filter_df.groupby("Customer ID").agg(
    recency=('Order Date', lambda date: (now_date - date.max()).days),
    frequency = ('Order ID','count'),
    Monetary = ('Total Revenue','sum')
    ).reset_index()

rfm['R_q']=pd.qcut(rfm['recency'],4,['1','2','3','4'])
rfm['F_q']=pd.qcut(rfm['frequency'],4,['4','3','2','1'])
rfm['M_q']=pd.qcut(rfm['Monetary'],4,['4','3','2','1'])
rfm['rfm_score']=rfm.R_q.astype(str) + rfm.F_q.astype(str) +rfm.M_q.astype(str)

rfm[rfm['rfm_score']=='111'].sort_values('Monetary',ascending=False)

