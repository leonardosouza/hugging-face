
import re
from transformers import pipeline

modelo = "csebuetnlp/mT5_multilingual_XLSum"

with open('conteudo.txt') as f:
    texto = f.read()

WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

resumo = pipeline("summarization", model=modelo)
resposta = resumo(WHITESPACE_HANDLER(texto))
print(resposta[0]['summary_text'])
