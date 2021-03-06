# -*- coding: utf-8 -*-
"""sentiment_index_copom.ipynb

"""

!pip install chart_studio

!pip install vaderSentiment

## packages need to be imported

import matplotlib.pyplot as plt
from chart_studio import plotly as py
import plotly.graph_objs as go
import pandas as pd
import requests
import json
from pandas.io.json import json_normalize

import datetime as DT
import requests
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import matplotlib.animation as animation
from nltk.corpus import stopwords

from chart_studio import plotly


data = pd.read_csv("data_clean.csv")

"""## Bert"""

X = data['cleaned_title'].to_list()

from transformers import BertTokenizer, BertForSequenceClassification

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone',num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')

labels = {0:'neutral', 1:'positive',2:'negative'}

sent_val = list()
for x in X:
    inputs = tokenizer(x, return_tensors="pt", padding=True, truncation=True,max_length=255, add_special_tokens = True)
    outputs = finbert(**inputs)[0]
   
    val = labels[np.argmax(outputs.detach().numpy())]
    print(x, '----', val)
    print('#######################################################')    
    sent_val.append(val)

"""## vader sentiment"""

## word count 

data['word_count'] = data['cleaned_title'].apply(lambda x: len(str(x).split(" ")))
data

analyser = SentimentIntensityAnalyzer()
neg=[]
pos=[]
neu=[]
compound=[]


for i in range(0,len(data)):
    #print(i)
    sentence=data['cleaned_title'][i]
    scores= analyser.polarity_scores(sentence)
    
    pos.append(scores['pos'])
    neg.append(scores['neg'])
    
    neu.append(scores['neu'])
    compound.append(scores['compound'])
   
data['positive']=pos 
data['negative']=neg
data['neutral']=neu
data['compound']=compound
    

data

compound_data=data.groupby('date')[['compound']].mean()



##The Compound score is a metric that calculates the sum of all the lexicon ratings 
#which have been normalized between -1(most extreme negative) and +1 (most extreme positive). 

compound_data

## sentiment compounded score.
import plotly.offline as py

senti = [go.Scatter( x = compound_data.index, y = compound_data['compound'] )]

layout1 = dict(title = 'Sentiment Score Plot')

fig = dict (data = senti, layout = layout1)
py.plot(fig)

"""#BERT

## Extract Sentiment
- https://towardsdatascience.com/how-nlp-has-evolved-for-financial-sentiment-analysis-fb2990d9b3ed
"""

!pip install transformers

from transformers import BertTokenizer, BertForSequenceClassification
import torch

"""article on tokenizers:https://towardsdatascience.com/tokenizers-nlps-building-block-9ab17d3e6929"""

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

label_list=['positive','negative','neutral']

inputs = tokenizer(data['cleaned_title'][1], return_tensors="pt", padding=True, truncation=True,max_length=50, add_special_tokens = True)
outputs = model(**inputs)
label_list[torch.argmax(outputs[0])]

headlines_list=list(data['cleaned_title'])

inputs = tokenizer(data['cleaned_title'][2], return_tensors="pt", padding=True, truncation=True,max_length=50, add_special_tokens = True)
outputs = model(**inputs)
label_list[torch.argmax(outputs[0])]
scoree= torch.argmax(outputs[0])
scoree

torch.max(outputs[0])

from torch.nn import functional as F
from transformers import BertTokenizer, BertForNextSentencePrediction
import torch

data['sent']="none"
data['sent2']=""

for i in range(0,len(data)):
   # print(i)
    sentence=tokenizer(data['cleaned_title'][i], return_tensors="pt" , padding=True, truncation=True,max_length=512, add_special_tokens = True)
    outputs = model(**sentence)
    scores= label_list[torch.argmax(outputs[0])]
    scoree= torch.max(outputs[0])
    #if sent==0: sentSum+=1
    #elif sent==1: sentSum-=1
    
    data['sent'][i]=scores
    data['sent2'][i]=scoree


    
    
   
    

data

df = data

print(df['sent'].value_counts())
