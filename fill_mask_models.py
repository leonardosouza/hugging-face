from transformers import pipeline
from pprint import pprint

modelos = [
    {
        "nome": "FacebookAI/xlm-roberta-base",
        "token": "<mask>"
    },
    {
        "nome": "neuralmind/bert-base-portuguese-cased",
        "token": "[MASK]"
    },
    {
        "nome": "pucpr/biobertpt-clin",
        "token": "[MASK]"
    }
]

for dict_model in modelos:
    model = dict_model['nome']
    token = dict_model['token']
    print(f'Testando o modelo {model}')
    modelo = pipeline("fill-mask", model=model)
    frase = f"Ando {token} porque já tive pressa!"

    predicoes = modelo(frase)
    # pprint(predicoes)

    for predicao in predicoes:
        resposta = predicao['token_str']
        score = predicao['score'] * 100
        frase = predicao['sequence']
        print(f'Predição "{resposta}" com score {score:.2f}% -> {frase}')
    print(f'\n=======')