# Projeto Hugging Face

Este projeto é uma coleção de scripts Python que demonstram a utilização de modelos da Hugging Face para diferentes tarefas de Processamento de Linguagem Natural (PLN). Ele inclui exemplos de implementação de um chatbot interativo e funcionalidades de preenchimento de máscara, utilizando tanto a biblioteca `transformers` diretamente quanto a API de Inferência da Hugging Face.

## Funcionalidades

- **Chatbot Interativo (Streamlit)**: Um chatbot construído com Streamlit (`app_chatbot.py`) que se conecta à API de Inferência da Hugging Face. Ele permite interagir com modelos como `Mixtral-8x7B-Instruct-v0.1` e `Google Gemma-7b-it`.
- **Chatbot Básico**: Um exemplo mais simples de chatbot (`my_chatbot.py`) utilizando a biblioteca `transformers` com o modelo `Felladrin/Llama-68M-Chat-v1`.
- **Preenchimento de Máscara (Fill-Mask)**: Demonstrações de como utilizar modelos para preencher palavras mascaradas em frases.
    - `fill_mask_default.py`: Exemplo básico utilizando o modelo `distilbert/distilroberta-base`.
    - `fill_mask_models.py`: Exemplos que iteram sobre diferentes modelos de preenchimento de máscara, como `FacebookAI/xlm-roberta-base`, `neuralmind/bert-base-portuguese-cased` e `pucpr/biobertpt-clin`.
- **API de Inferência**: Um script (`inference_api.py`) que demonstra como interagir diretamente com a API de Inferência da Hugging Face para realizar chamadas a modelos.
- **Uso Direto da Biblioteca Transformers**: O script `transformer.py` mostra o uso direto da biblioteca `transformers` para carregar e tokenizar modelos.
- **Tradução de Texto**: O script `translation.py` demonstra a utilização do modelo `facebook/mbart-large-50-many-to-many-mmt` para traduzir textos do português para outras línguas.

## Como Rodar

### Pré-requisitos

- Python 3.8 ou superior
- Uma conta no Hugging Face e um `HF_ACCESS_TOKEN` (para usar a API de Inferência).

### Configuração

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/leonardosouza/hugging-face.git
   cd hugging-face
   ```

2. **Crie e ative o ambiente virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Linux/macOS
   # .venv\Scripts\activate  # No Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```
   *(Observação: um arquivo `requirements.txt` não está presente no repositório, mas é uma boa prática criá-lo com as dependências `streamlit`, `transformers`, `python-dotenv`, `requests`)*

4. **Configure seu token de acesso da Hugging Face**:
   Crie um arquivo `.env` na raiz do projeto e adicione seu token de acesso:
   ```
   HF_ACCESS_TOKEN="hf_YOUR_HUGGING_FACE_TOKEN"
   ```

### Executando os Scripts

- **Para rodar o Chatbot Streamlit**:
   ```bash
   streamlit run app_chatbot.py
   ```

- **Para rodar outros scripts (ex: `inference_api.py`)**:
   ```bash
   python inference_api.py
   ```

- **Para rodar o script de Tradução**:
   ```bash
   python translation.py
   ```

## Estrutura do Projeto

- `README.md`: Este arquivo.
- `app_chatbot.py`: Implementação do chatbot interativo com Streamlit.
- `fill_mask_default.py`: Exemplo de preenchimento de máscara com modelo padrão.
- `fill_mask_models.py`: Exemplos de preenchimento de máscara com múltiplos modelos.
- `inference_api.py`: Exemplo de interação com a API de Inferência da Hugging Face.
- `main.py`: Ponto de entrada principal (atualmente simples).
- `my_chatbot.py`: Exemplo de chatbot básico.
- `restrict_models.py`: (Atualmente vazio) Pode ser usado para definir restrições de modelos, ou para registrar quais modelos específicos estão sendo utilizados.
- `summary.py`: Script que utiliza o modelo `csebuetnlp/mT5_multilingual_XLSum` para gerar resumos de texto a partir do `conteudo.txt`.
- `transformer.py`: Exemplo de uso direto da biblioteca `transformers`.
- `translation.py`: Script para demonstração de tradução de texto.
- `conteudo.txt`: Arquivo de texto contendo o conteúdo a ser resumido pelo `summary.py`.
- `requirements.txt`: Lista as dependências do projeto, como `streamlit`, `transformers`, `python-dotenv` e `requests`, essenciais para a execução dos scripts.
- `.env`: Arquivo para variáveis de ambiente (token de acesso da Hugging Face).
- `.gitignore`: Arquivo para ignorar arquivos e diretórios específicos no controle de versão.
- `.python-version`: Define a versão do Python usada (geralmente para `pyenv`).
- `.venv/`: Diretório do ambiente virtual.

---
**Desenvolvido por: [Seu Nome/Organização]**
