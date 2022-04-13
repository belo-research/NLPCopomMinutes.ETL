# NLP_Copom_Minutes
The script aims to automatise the process of sequentially generating NLP_Copom_Minutes dashboard Data, by parsing the PDF's, generate input data and update the dashboard.
# Concept
Belo use Natural language Processing techniques to analyse the transcripts of minutes of meetings of the Banco Central do Brasil's (BAECN) 
Approximately every 45 days, the Monetary Policy Committee (COPOM) of the Central Bank of Brazil (BACEN) meets to define the target for the Brazilian basic interest rate (Selic). One of the products of this meeting is the draft, which we used in this project to extract information on Brazilian monetary policy through Natural Language Processing (NLP).
## Sections:
#### 1- sentiment analysis:
The sentiment analysis is the use of natural language processing, text analysis, computational linguistics, and biometrics to systematically identify, extract, quantify, and study affective states and subjective information.

The main objective of this sentiment analysis is to measure how confident COPOM is in the Brazilian economy through a numerical value.
#### 2- Topic Analysis:
The Topic analysis uses machine learning methods to classify discourse into discrete clusters. The resulting clusters are then labelled based on the terms most associated with each cluster. Given the presence of certain terms which are heavily used (e.g. Inflation, Price) and associated with all topics, to better identify the composition of each topic the score is modified to show the relative rather than absolute importance of a term to each topic. This is done by taking the log ratio of importance for each highly relevant term (filtered based on abosulte importance) between clusters, with the score representing the average log ratio of importance. Roughly the score corresponds to the average importance of that term relevant to all other scores. A score of 1 therefore roughly to a given score being twice as relevant on average to the topic compared with all other topics.

## Instalation 
Inside your environment (conda, venv, etc):

pip install -r requirements.txt

## How to run
Folder 'ETL' contains the data downloader to get the dat aand clean it.
Folder 'Data' contains the raw data .
Folder 'Transformed data' contains the data ready to create the vizualiations.
Folder 'Data transformation' contains the code with the parsers for sentiment analysis and topic analysis, and the detailed description step by step.

## Link to dashboard
https://observablehq.com/d/e9caed123eaf963c
