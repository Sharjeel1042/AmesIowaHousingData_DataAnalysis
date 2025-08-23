import pandas as pd
import numpy as np

df=pd.read_csv('AmesHousing.csv',keep_default_na=False, na_values=[""])
df.columns = df.columns.str.strip().str.lower()
#Handling null values
df['lot frontage']=df.groupby('neighborhood')['lot frontage'].transform(lambda x: x.fillna(x.median()))
df['alley']=df['alley'].fillna('None')
df['garage yr blt']=df['garage yr blt'].fillna(0)
df['garage finish']=df['garage finish'].fillna('NA')
df['garage cars']=df['garage cars'].fillna(0)
df['garage area']=df['garage area'].fillna(0)
df['garage qual']=df['garage qual'].fillna('NA')
df['garage cond']=df['garage cond'].fillna('NA')
df['bsmt qual']=df['bsmt qual'].fillna('NA')
df['bsmt cond']=df['bsmt cond'].fillna('NA')
df['bsmt exposure']=df['bsmt exposure'].fillna('NA')
df['bsmtfin type 1']=df['bsmtfin type 1'].fillna('NA')
df['bsmtfin sf 1']=df['bsmtfin sf 1'].fillna(0)
df['bsmtfin type 2']=df['bsmtfin type 2'].fillna('NA')
df['bsmtfin sf 2']=df['bsmtfin sf 2'].fillna(0)
df['bsmt unf sf']=df['bsmt unf sf'].fillna(0)
df['total bsmt sf']=df['bsmtfin sf 1']+df['bsmtfin sf 2']+df['bsmt unf sf']
df['bsmt full bath']=df['bsmt full bath'].fillna(0)
df['bsmt half bath']=df['bsmt half bath'].fillna(0)


#DataType Handling
df['garage yr blt']=pd.to_numeric(df['garage yr blt']).astype(int)

#Dropping nulls from mas vnr type/mas vnr area and lot frontage(26 rows~0.9% of total data. This wont affect the results by a great deal)
df=df.dropna(subset=['lot frontage','mas vnr type','mas vnr area'])

df.to_csv('AmesHousingCleaned.csv',index=False)
df_cleaned=df.copy()

df_cleaned.info()
#df.info()