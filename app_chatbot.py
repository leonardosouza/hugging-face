from dotenv import find_dotenv, load_dotenv
from transformers import AutoTokenizer
import os
import requests
import streamlit as st

load_dotenv(find_dotenv())
token = os.environ['HF_ACCESS_TOKEN']
headers = { 'Authorization': f'Bearer {token}' }

modelos = {
    'mistralai/Mixtral-8x7B-Instruct-v0.1': '[/INST]',
    'google/gemma-7b-it': '<start_of_turn>model\n'
}

modelo = st.selectbox('Selecione um modelo', options=modelos)

url = f'https://api-inference.huggingface.co/models/{modelo}'

print(modelo)
if ('modelo_atual' not in st.session_state or st.session_state['modelo_atual']):
    st.session_state['modelo_atual'] = modelo

if 'mensagens' not in st.session_state:
    st.session_state['mensagens'] = []

modelo_escolhido = st.session_state['modelo_atual']
token_modelo = modelos[modelo_escolhido]
tokenizer_mixtral = AutoTokenizer.from_pretrained(modelo_escolhido)

area_chat = st.empty()
mensagem = st.chat_input('Faça sua pergunta aqui:')
if mensagem:
    st.session_state['mensagens'].append({"role": "user", "content": mensagem })
    template = tokenizer_mixtral.apply_chat_template(st.session_state['mensagens'], tokenize=False, add_generation_prompt=True)
    json = {
        'inputs': template,
        'parameters': {
            'max_new_tokens': 1000
        },
        'options': { 'use_cache': False, 'wait_for_model': True }
    }

    response = requests.post(url, json=json, headers=headers).json()
    if response['error']:
        mensagem_chatbot = response['error']
    else: 
        mensagem_chatbot = response[0]['generated_text'].split(token_modelo)[-1]
    st.session_state['mensagens'].append({"role": "assistant", "content": mensagem_chatbot })

    
with area_chat.container():
    for mensagem in st.session_state['mensagens']:
        chat = st.chat_message(mensagem['role'])
        chat.markdown(mensagem['content'])

print(st.session_state['mensagens'])
