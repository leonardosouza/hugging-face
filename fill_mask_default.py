from transformers import pipeline
from pprint import pprint

modelo = pipeline("fill-mask", model="distilbert/distilroberta-base")

frase = "The capital of <mask> is Brasilia."

predicoes = modelo(frase)
# pprint(predicoes)

for predicao in predicoes:
    resposta = predicao['token_str']
    score = predicao['score'] * 100
    frase = predicao['sequence']
    print(f'Predição "{resposta}" com score {score:.2f}% -> {frase}')