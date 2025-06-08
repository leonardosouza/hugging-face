from transformers import pipeline

modelo = 'facebook/mbart-large-50-many-to-many-mmt'
mensagens = [
    "Olá! Estou aprendendo a utilizar modelos de IA do Hugging Face",
    "Como vai você? Eu preciso saber da sua vida!"
]
linguas = ['en_XX', 'es_XX', 'fr_XX']
tradutor = pipeline(task='translation', model=modelo)

for lingua in linguas:
    print('\n', '==='*5, f'Traduzindo para {lingua}', '==='*5)
    traducoes = tradutor(mensagens, src_lang='pt_XX', tgt_lang=lingua)
    for mensagem, traducao in zip(mensagens, traducoes):
        print('\nFrase original', mensagem)
        frase_traduzida = traducao['translation_text']
        print(f'Frase em {lingua}: "{frase_traduzida}"')