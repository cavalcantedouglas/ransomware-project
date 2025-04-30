# ransomware-project
Este projeto tem como objetivo simular o funcionamento basico de um ransomware

## ⚠️ Aviso

Este projeto **não deve** ser usado em sistemas reais ou de terceiros. É um exercício de aprendizado sobre segurança ofensiva e criptografia.

## Tecnologias usadas

- Python 3.10+
- Biblioteca `cryptography` (Fernet)

## Como funciona

- `encrypt.py`: criptografa todos os arquivos de uma pasta alvo e gera uma chave (`chave.key`) e uma nota de resgate (`nota.txt`).
- `decrypt.py`: descriptografa os arquivos usando a chave gerada.




