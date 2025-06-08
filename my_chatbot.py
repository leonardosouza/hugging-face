from transformers import pipeline

chatbot = pipeline('text-generation', 'Felladrin/Llama-68M-Chat-v1')

mensagem_sistema = "You area a helpful artifical intelligence."
prompt_sistema = f"<|im_start|>system\n{mensagem_sistema}<|im_end|>\n"

pergunta_usuario = "How can I become a Python programer?"
prompt_usuario = f"<|im_start|>user\n{pergunta_usuario}<|im_end|>\n"

prompt_assistant = f"<|im_start|>assistant"

conversa = f"{prompt_sistema}{prompt_usuario}{prompt_assistant}"

resposta = chatbot(conversa)

print(resposta[0]['generated_text'])