from os import name
import os
import requests
import json
from requests.api import request
import streamlit as st
import pandas as pd

url = "{}".format(os.environ.get('PG_API_URL'))

st.title('Amazing Question Answering Thing!')

if st.button('Currently available models!'):
    newurl=url + 'models'
    response=requests.request("GET",newurl)
    models=response.json()
    for m in models:
        st.success(m['name'])


if st.title('Add a model'):
    name=st.text_input('name')
    tokenizer= st.text_input('tokenizer')
    model=st.text_area('model')
    if st.button('Hit to add'):
        newurl=url + 'models'
        payload=json.dumps({
            "name":name,
            "tokenizer":tokenizer,
            "model":model
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("PUT", newurl, headers=headers, data=payload)
        st.success("Successfully added new model '{}'".format(response.json()[-1]['name']))

if st.button('Delete a model'):
    allmodels=url + 'models'
    response=requests.request("GET",allmodels)
    models=response.json()
    modellist=[]
    for m in models:
        modellist.append(m['name'])
    option=st.selectbox('Select a model',modellist)
    st.write('You have selected:',option)
    if st.button('Are you sure you want to delete the selected model'):
        updatedurl=url + 'models' + '?model=' + option
        response1=requests.request("DELETE",updatedurl)
        st.success("Successfully deleted model '{}'".format(option))

# Inputs
question = st.text_input('Question')
context = st.text_area('Context')

# Execute question answering on button press
if st.button('Answer Question'):
    newurl=url + 'answer'
    payload = json.dumps({
        "question": question,
        "context": context
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", newurl, headers=headers, data=payload)
    answer = response.json()['answer']

    st.success(answer)

uploaded_file = st.file_uploader("Choose a file to upload")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    answer_list=[]
    for index,row in df.iterrows():
        newurl=url + 'answer'
        question = row['question']
        context = row['context']
        payload = json.dumps({
        "question": question,
        "context": context
        })
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", newurl, headers=headers, data=payload)
        answer = response.json()['answer']
        row['finalanswer'] = answer
        answer_list.append(answer)
    df['finalanswer']=answer_list
    st.table(df)      
