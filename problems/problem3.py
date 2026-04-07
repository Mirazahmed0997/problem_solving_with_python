
import pandas as pd

df= pd.DataFrame({'list':[1,2,3,4]})

sqr_list=df['list'].map(lambda x: x*x)

print(sqr_list)