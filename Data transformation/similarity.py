# -*- coding: utf-8 -*-
"""similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wkv0qZkfzyR2QXAVNchBLiIOqp2LzYRb
"""

import pandas as pd

"""## using similarity to classify our topics automatically without human intervention
### the idea is to creat dic with 4 topics then we use our new data each time to calculate the similarity between these new topics and the old topics so we could figure out the name of each topic.
"""

topics = pd.read_csv("/content/topic_compistion (1).csv")
topics = topics [["Term","Topic"]]
topics

topics.Topic.unique()

topic1 = topics[topics["Topic"]=="Policy Intervention"]
topic2 = topics[topics["Topic"]=="Inflation Growth"]
topic3 = topics[topics["Topic"]=="Exchange Rate"]
topic4 = topics[topics["Topic"]=="Economic Growth"]

topic1_term = ' '.join(topic1['Term'].tolist())
topic2_term = ' '.join(topic2['Term'].tolist())
topic3_term = ' '.join(topic3['Term'].tolist())
topic4_term = ' '.join(topic4['Term'].tolist())

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# returns the cosine similarity value of the two given texts
def compute_cosine_similarity(text1, text2):
    
    # stores text in a list
    list_text = [text1, text2]
    
    # converts text into vectors with the TF-IDF 
    vectorizer = TfidfVectorizer(stop_words='english')
    vectorizer.fit_transform(list_text)
    tfidf_text1, tfidf_text2 = vectorizer.transform([list_text[0]]), vectorizer.transform([list_text[1]])
    
    # computes the cosine similarity
    cs_score = cosine_similarity(tfidf_text1, tfidf_text2)
    
    return np.round(cs_score[0][0],2)

# use function to compute cosine similarity
cosine_similarity12 = compute_cosine_similarity(topic1_term,topic2_term)
cosine_similarity13 = compute_cosine_similarity(topic1_term,topic3_term)
cosine_similarity14 = compute_cosine_similarity(topic1_term,topic4_term)
cosine_similarity23 = compute_cosine_similarity(topic2_term,topic3_term)
cosine_similarity24 = compute_cosine_similarity(topic2_term,topic4_term)
cosine_similarity34 = compute_cosine_similarity(topic3_term,topic4_term)

# print results
print('The cosine similarity of topic 1 and 2 is {}.'.format(cosine_similarity12))
print('The cosine similarity of topic 1 and 3 is {}.'.format(cosine_similarity13))
print('The cosine similarity of topic 1 and 4 is {}.'.format(cosine_similarity14))
print('The cosine similarity of topic 3 and 2 is {}.'.format(cosine_similarity23))
print('The cosine similarity of topic 2 and 4 is {}.'.format(cosine_similarity24))
print('The cosine similarity of topic 3 and 4 is {}.'.format(cosine_similarity34))

"""## using similarity to track chnages through time"""

data = pd.read_csv("data_clean.csv")

data['similarity_change']=""

for i in range(1,len(data)):

  # print(i)
  cosine_similarity12 = compute_cosine_similarity(data['cleaned_title'][i],data['cleaned_title'][i-1])
  print(cosine_similarity12)
  data['similarity_change'][i]=cosine_similarity12

data

import altair as alt
base = alt.Chart( data).encode(x='date:T')


line =  base.mark_line().encode(
    y=alt.Y('similarity_change:Q', axis=alt.Axis( title='similarity_change', ))
)
line

