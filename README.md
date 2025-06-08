# Projeto Hugging Face

Este projeto serve como um *playground* e demonstração prática de diversas aplicações de Processamento de Linguagem Natural (PLN) utilizando a biblioteca `transformers` e a API de Inferência da Hugging Face. Ele abrange desde a criação de chatbots interativos e básicos até o preenchimento de máscaras em texto, sumarização e tradução, explorando diferentes modelos e suas implementações.

## Funcionalidades

- **Chatbot Interativo (Streamlit)**: O `app_chatbot.py` implementa um chatbot interativo utilizando Streamlit e a API de Inferência da Hugging Face. Este chatbot permite a seleção e interação com modelos de linguagem avançados como `mistralai/Mixtral-8x7B-Instruct-v0.1` e `google/gemma-7b-it`.
- **Chatbot de Linha de Comando (API de Inferência)**: O `inference_api.py` demonstra a integração direta com a API de Inferência da Hugging Face para criar um chatbot de linha de comando. Ele utiliza o modelo `mistralai/Mixtral-8x7B-Instruct-v0.1` para responder a perguntas do usuário.
- **Chatbot Básico (Transformers)**: O `my_chatbot.py` é um exemplo mais simples de chatbot, que utiliza a `pipeline` de `text-generation` da biblioteca `transformers` com o modelo `Felladrin/Llama-68M-Chat-v1` para gerar respostas.
- **Sumarização de Texto**: O `summary.py` demonstra como gerar resumos de texto a partir de um arquivo de entrada (`conteudo.txt`) utilizando o modelo `csebuetnlp/mT5_multilingual_XLSum` da Hugging Face.
- **Tradução de Texto**: O `translation.py` exemplifica a tradução de texto entre múltiplos idiomas. Ele utiliza o modelo `facebook/mbart-large-50-many-to-many-mmt` para traduzir frases do português para outras línguas.
- **Preenchimento de Máscara (Fill-Mask)**: Este projeto inclui demonstrações detalhadas de como usar modelos para preencher palavras mascaradas em frases.
    - `fill_mask_default.py`: Um exemplo básico que utiliza o modelo `distilbert/distilroberta-base` para preencher uma máscara em uma frase simples.
    - `fill_mask_models.py`: Um script que itera sobre e demonstra o uso de múltiplos modelos de preenchimento de máscara, incluindo `FacebookAI/xlm-roberta-base`, `neuralmind/bert-base-portuguese-cased` e `pucpr/biobertpt-clin`.
- **Uso Direto da Biblioteca Transformers**: O `transformer.py` ilustra o carregamento e a tokenização de modelos diretamente com as classes `AutoTokenizer` e `AutoModel` da biblioteca `transformers`, utilizando como exemplo o modelo `FacebookAI/xlm-roberta-base`.

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

- **Para rodar o Chatbot de Linha de Comando (API de Inferência)**:
   ```bash
   python inference_api.py
   ```

- **Para rodar o Chatbot Básico**:
   ```bash
   python my_chatbot.py
   ```

- **Para rodar o script de Sumarização**:
   ```bash
   python summary.py
   ```

- **Para rodar o script de Tradução**:
   ```bash
   python translation.py
   ```

- **Para rodar os exemplos de Preenchimento de Máscara**:
   ```bash
   python fill_mask_default.py
   python fill_mask_models.py
   ```

- **Para rodar o exemplo de Uso Direto da Biblioteca Transformers**:
   ```bash
   python transformer.py
   ```

## Estrutura do Projeto

- `README.md`: Este arquivo detalha o projeto, suas funcionalidades, como configurá-lo e executá-lo.
- `app_chatbot.py`: Implementa um chatbot interativo utilizando Streamlit para interação com modelos da Hugging Face via API de Inferência.
- `inference_api.py`: Contém um exemplo de chatbot de linha de comando que interage diretamente com a API de Inferência da Hugging Face.
- `my_chatbot.py`: Um script que demonstra um chatbot básico utilizando a biblioteca `transformers` para geração de texto.
- `summary.py`: Script para sumarização de texto, utilizando modelos da Hugging Face para gerar resumos a partir de um arquivo de entrada.
- `translation.py`: Demonstra a funcionalidade de tradução de texto entre múltiplos idiomas utilizando modelos da Hugging Face.
- `fill_mask_default.py`: Um exemplo simples de preenchimento de máscara com um modelo padrão.
- `fill_mask_models.py`: Demonstração avançada de preenchimento de máscara, explorando múltiplos modelos para esta tarefa.
- `transformer.py`: Exemplifica o uso direto de componentes da biblioteca `transformers`, como `AutoTokenizer` e `AutoModel`.
- `conteudo.txt`: Arquivo de texto contendo o conteúdo a ser utilizado pelo script `summary.py` para gerar resumos.
- `requirements.txt`: Lista todas as dependências Python necessárias para o projeto, permitindo uma fácil instalação.
- `main.py`: O ponto de entrada principal do projeto, atualmente com uma funcionalidade básica.
- `restrict_models.py`: (Atualmente vazio) Pode ser utilizado para definir restrições de modelos ou registrar quais modelos específicos estão sendo empregados no projeto.
- `index.html`: Um arquivo HTML que pode ser a base para uma interface web, embora suas funcionalidades não sejam diretamente integradas aos scripts Python principais.
- `.env`: Arquivo para armazenar variáveis de ambiente sensíveis, como o token de acesso da Hugging Face.
- `.gitignore`: Configura arquivos e diretórios a serem ignorados pelo controle de versão do Git.
- `.python-version`: Usado para especificar a versão do Python, comum em gerenciadores como `pyenv`.
- `.venv/`: O diretório do ambiente virtual Python, onde as dependências do projeto são instaladas.

---
**Desenvolvido por: Leonardo Souza**
