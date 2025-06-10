from textwrap import wrap
import textwrap
from transformers import pipeline
from tabulate import tabulate

modelo = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"

reviews = [
    "Que é muito caro, mas vale cada tostao.",
    "Não tenho dinheiro para comprar este produto é uma vergonha um celular custando isso, vou comprar um Galaxy s23 é muito melhor.",
    "Produto de excelência!!! Retirada na loja, sem burocracia e funcionários bem educados e ágeis, logo disponibilizaram o aparelho após conferirem o pedido. Sobre o produto, quem já é cliente Apple tem conhecimento de causa e sabe da qualidade, indico o investimento sabendo que sim terá um ótimo retorno para o que deseja.",
    "Magalu vai levar uma estrela porque paguei mais caro para ter o celular em 2 horas, me atrasaram mais de 24hs. Nunca compro nesta loja. ",
    "Comprei Apple iPhone 16 pro max 256 gb titânio preto 6,9 48 mp iOS 5 g tá com 5 meses a câmera frontal parou de funcionar, estou precisando saber como faço pra falar com os responsáveis da assistência",
    "Custo benefício não vale apena!",
    "Produto atende, mas não é o estado da arte!"
]


classificador = pipeline('text-classification', model=modelo)

emojis = {
    "positive": "😊​",
    "negative": "🙁​",
    "neutral": "😐​"
}

grupos = {
    "positive": [],
    "negative": [],
    "neutral": []
}

for review in reviews:
    resultado = classificador(review)
    grupos[resultado[0]['label']].append(f"{emojis[resultado[0]['label']]} ({round(resultado[0]['score'] * 100, 1)}%) =>  {textwrap.fill(review, width=40)}")

print(tabulate({"Positivo": grupos['positive'], "Neutro": grupos['neutral'], "Negativo": grupos['negative']}, headers="keys", tablefmt="grid"))