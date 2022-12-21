# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 22:33:40 2022

@author: eevee
"""
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing dataframe
df= pd.read_csv('GoodReadsData.csv')

#streamlit basic configurations
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

    
st.sidebar.header('My Year in Books')

st.sidebar.subheader('Genre parameter')
genre_selection = st.sidebar.selectbox('Selection', ('Adventure','Fantasy','Fiction','Historical Fiction','Memoir','Mystery','Science Fiction','Thriller'))

st.sidebar.markdown('''
---
Created with ❤️ by Eevee Murdock
''')

#basic stats
totalpages= str(df['Pages'].sum())

maxpages=str(df['Pages'].max())
minpages=str(df['Pages'].min())

avgpages=str(round(df['Pages'].mean()))

avgdays=str(round(df['Days'].mean()))
mindays=str(df['Days'].min())

lastyr=3040
difference = str(int(totalpages)-lastyr)

# Stats
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Longest Book", maxpages )
col2.metric("Total Pages", totalpages, difference)
col3.metric("Average Days Per Book",avgdays)

#genre filter
st.markdown('### Books of Selected Genre')
genre_filter = df['Genre'] == genre_selection
genre_df = df[genre_filter]
st.dataframe(genre_df)

#Days Graph

days = df['Days']
pages = df['Pages']

fig, ax = plt.subplots(figsize=(7, 3))

plt.plot(days,pages, 'go')
plt.title('Page Count vs Days to Read')
plt.ylabel('pages')
plt.xlabel('days')

st.pyplot(fig)



#Genre Graph
gb = df.groupby('Genre')

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
st.pyplot(f)