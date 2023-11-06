#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from html_table_parser.parser import HTMLTableParser
from html.parser import HTMLParser
from pprint import pprint as pp
import pandas as pd
import urllib.request as ur
req=ur.Request('https://www.indiatoday.in/sports/cricket/story/world-cup-2023-india-vs-pakistan-live-score-updates-commentary-rohit-sharma-babar-azam-ahmedabad-2448793-2023-10-14')
s=ur.urlopen(req)
rd=s.read().decode('utf-8')
c=HTMLTableParser()
c.feed(rd)
df=pd.DataFrame(c.tables[1])
print(df)
ans=input("dou you want to save this?(Y/N)")
if ans == 'Y':
    df.to_csv("indvspak.csv")
import re
def word_search(sentence,word):
    y=" "
    for w in word:
        if re.search(w,sentence):
           y=w
    return y
import pandas as pd
data=pd.read_csv("indvspak_inn1.csv",usecols=['Ball','Runs','Ball_Number','Over_No','Bowler_Name','Batsman_Name','Score','Batsman_Style','Dismissal_Type','Howout','Dismissed','Extras_Runs'])
data=data.dropna(subset=['Ball_Number'])
#word=['full','tossed','short','good length','In the slot','length']
#word=['cover','sweeper cover','square','bowler','point','off side','mid on','mid off','mid-wicket','long off','long on','deep point','third man','extra cover','fine leg','deep cover','deep backward point','cover-point','deep backward square leg','backward point','short mid-wicket','short fine leg','deep square leg','fine leg','silly mid on','square leg','corner']
#data['field']=data['Commentary'].apply(lambda x:word_search(x,word))
data.to_csv("C:/Users/Public/indvspak/1st_inn_gen_stats.csv")
print(data.info(),"\n",data)

