__author__ = 'marc' 

import pandas as pd 
df= pd.DataFrame([['foo','foo','bar','bar','bar','oats'],[1.0,2.0,1.0,4.0,4.0,5.0],[2.0,3.0,4.0,5.0,1.0,5.0]]).T 


df.columns=['mycat','var1','var2']
df.var1=df.var1.astype('int64') 
df.var2=df.var2.astype('int64')


test=df.groupby('mycat', as_index=False).var2.count()

print test