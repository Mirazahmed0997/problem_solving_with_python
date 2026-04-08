import pandas as pd

df=pd.DataFrame({'list':[1,2,3,4,5,6,7,8,9,10]})



evens= pd.Series(filter(lambda x: x%2==0,df['list']))

sqr_even= evens.map(lambda x: x*x)

print(evens)
print(sqr_even)



df = pd.DataFrame({'set':[2,4,2,4,5,4,8,9,76,79,67]})

odd_numb = pd.Series(filter(lambda x: x%2==1,df['set']))

odd_sqr= odd_numb.map(lambda x : x*x)

print(odd_numb)
print(odd_sqr)
