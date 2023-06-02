import pandas as pd
df=pd.read_stata('./CGSS2021.dta',convert_categoricals=False, convert_missing=True)
respondent=df.loc[:,['A7a','A2','A3_1','A10','A18','A43','A8a','A58']]
print(df.head())