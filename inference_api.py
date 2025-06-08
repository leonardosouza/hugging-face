import requests
from transformers import AutoTokenizer
from pprint import pprint
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
token = os.environ['HF_ACCESS_TOKEN']

modelo = 'mistralai/Mixtral-8x7B-Instruct-v0.1'

chat = []

tokenizer_mixtral = AutoTokenizer.from_pretrained(modelo)
headers = { 'Authorization': f'Bearer {token}' }
url = f'https://api-inference.huggingface.co/models/{modelo}'

while True:
    mensagem = input('Faça sua pergunta (digite "q" para sair): ')
    if mensagem == 'q':
        break
    chat.append({"role": "user", "content": mensagem })
    template = tokenizer_mixtral.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
    json = {
        'inputs': template,
        'parameters': {
            'max_new_tokens': 1000
        },
        'options': { 'use_cache': False, 'wait_for_model': True }
    }

    response = requests.post(url, json=json, headers=headers).json()
    
    if response['error']:
        print(response['error'])
        break
    else:
        mensagem_chatbot = response[0]['generated_text'].split('[/INST]')[-1]
        print('Resposta do bot: ', mensagem_chatbot)
        chat.append({"role": "assistant", "content": mensagem_chatbot })

pprint(f'\nFull conversation: {chat}')