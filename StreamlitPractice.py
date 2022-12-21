# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:22:32 2022

@author: eevee
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataframe
df= pd.read_csv('GoodReadsData.csv')

#filter by fiction
fiction_filter = df['Genre'] == 'Fiction'
fiction_df = df[fiction_filter]
fiction_df

#filter by length
length_filter = df['Pages'] >=400
long_df = df[length_filter]
long_df

#basic stats
totalpages= df['Pages'].sum()
print("Total Pages Read: ", totalpages)
maxpages=df['Pages'].max()
print("Longest Book Length: ",maxpages)
avgpages=df['Pages'].mean()
print("Average Number of Pages/Book: ",avgpages)
avgdays=df['Days'].mean()
print("Average Number of Days/Book: ",avgdays)

#page count vs days to read graph
days = df['Days']
pages = df['Pages']

plt.plot(days,pages, 'go')
plt.title('Page Count vs Days to Read')
plt.ylabel('pages')
plt.xlabel('days')

#stats by genre
gb = df.groupby('Genre')
gb.size()
genrestats=gb.agg(['mean','sum'])
genrestats

#genre count
gb.size()

#graph by genre
l = ['Adventure','Fantasy','Fiction','Historical Fiction','Memoir','Mystery','Science Fiction','Thriller']
pgs=[]
for i in l:
  key = i 
  df1 = gb.get_group(key)
  x=df1['Pages'].sum()
  pgs.append(x)

ps={'Genre':l,'Total Pages Read':pgs}
pagestats=pd.DataFrame(ps)
pagestats=pagestats.sort_values(by=['Total Pages Read'], ascending=False)

f=plt.figure()
f.set_figwidth(12)
plt.bar(pagestats['Genre'],pagestats['Total Pages Read'])
plt.xlabel('Genre')
plt.ylabel('Total Pages')
plt.title('Pages Read by Genre')

