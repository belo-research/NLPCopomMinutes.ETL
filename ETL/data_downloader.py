# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 12:52:29 2022

@author: ThinkPad
"""

################

import pandas as pd

### Step 1 - download the data

import urllib.request, json 

urla="https://www.bcb.gov.br/api/servico/sitebcb/copomminutes/"

urlb="ultimas?quantidade=2000&filtro="

urlc=urla+urlb

with urllib.request.urlopen(urlc) as url:
    data = json.loads(url.read().decode())
    print(data)


path=r'C:\Users\ThinkPad\Documents\rescarh\nlp_application\copom_data\pdfs\pdf_'

with open(r'C:\Users\ThinkPad\Documents\rescarh\nlp_application\copom_data\pdfs\minutes_3103.txt', 'w') as convert_file:
     convert_file.write(json.dumps(data))

import urllib.request

pdf_path = ""

def download_file(download_url, path, filename):
    response = urllib.request.urlopen(download_url)    
    file = open(path + filename + ".pdf", 'wb')
    file.write(response.read())
    file.close()


for file in data['conteudo']: 
    file_urla="https://www.bcb.gov.br"+'%20'.join(file['Url'].split())
    filename=file['Titulo'].split()[0]
    file['key']= filename
    download_file(file_urla,path,filename)

################

### create pdf

matching_file=pd.DataFrame(data['conteudo'])
matching_file=matching_file[matching_file['key']!='Changes']

### Step 2 - download the data

import PyPDF2

def parse_text(filename,path):
    file=PyPDF2.PdfFileReader(path + filename)
    concat=[]
    for page in range(0,file.getNumPages()):
        pageObj = file.getPage(page) 
        text = pageObj.extractText()
        concat.append(text)
        
    return(' '.join(concat))

from tqdm import tqdm

for key in tqdm(matching_file.key.unique()):
    try:
        matching_file.loc[matching_file['key']==key,
                     'text']=parse_text( key +'.pdf',path)
    except:
        print(key)

matching_file.to_csv(r'C:\Users\ThinkPad\Documents\rescarh\nlp_application\copom_data' + '\copom_minutes_data.csv')
