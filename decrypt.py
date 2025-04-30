import os
from cryptography.fernet import Fernet

# Le a chave salva
try:
    with open("chave.key", "rb") as key_file:
        key = key_file.read()
    cipher = Fernet(key)
except FileNotFoundError:
    print("Erro: Arquivo de chave não encontrado.")
    exit(1)
except Exception as e:
    print(f"Erro ao ler a chave: {e}")
    exit(1)

pasta_alvo = "/home/douglas/importante"

# Contadores para acompanhar progresso
arquivos_sucesso = 0
arquivos_falha = 0

# Verifica se o diretório existe
if not os.path.exists(pasta_alvo):
    print(f"Erro: O diretório {pasta_alvo} não existe.")
    exit(1)

# Percorre todos os arquivos recursivamente
for root, dirs, files in os.walk(pasta_alvo):
    for nome_arquivo in files:
        caminho_arquivo = os.path.join(root, nome_arquivo)

        # Ignora arquivos irrelevantes
        if nome_arquivo in ["encrypt.py", "chave.py", "nota.txt", "decrypt.py"]:
            continue

        try:
            # Le, descripografa e salva o arquivo
            with open(caminho_arquivo, "rb") as file:
                conteudo_encriptado = file.read()
            conteudo = cipher.decrypt(conteudo_encriptado)
            with open(caminho_arquivo, "wb") as file:
                file.write(conteudo)
            print(f"Arquivo descriptografado: {caminho_arquivo}")
            arquivos_sucesso += 1
        except Exception as e:
            print(f"Erro ao descriptografar {caminho_arquivo}: {str(e)}")
            arquivos_falha += 1

# Mostra um resumo do processo de descriptografia
print(f"\nResumo da descriptografia:")
print(f"Arquivos processados com sucesso: {arquivos_sucesso}")
print(f"Arquivos com falha: {arquivos_falha}")

if arquivos_falha == 0:
    print("Todos os arquivos foram recuperados com sucesso!")
else:
    print("Atenção: Alguns arquivos não puderam ser descriptografados.")
