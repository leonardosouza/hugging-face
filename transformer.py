from transformers import AutoTokenizer, AutoModel

nome_modelo = 'FacebookAI/xlm-roberta-base'

modelo = AutoModel.from_pretrained(nome_modelo)
tokenizador = AutoTokenizer.from_pretrained(nome_modelo)

#print(modelo)
#print(tokenizador)

inputs = tokenizador("A linguagem <mask< é uma ferramenta sensacional.", return_tensors='pt')
#print(tokens)

ouputs = modelo(**inputs)
print(ouputs)