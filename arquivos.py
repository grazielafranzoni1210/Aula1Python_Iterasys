# 1- importação de pacotes
import json
import pytest

# 2- classes


# 3- definições (funções e métodos)
dados = {}

dados['cliente'] = []  # indica a criação de um vetor, matriz, lista...
dados['cliente'].append({'nome': 'Juca', 'telefone': '11999999999', 'email': 'juca@gmail.com.br'})
dados['cliente'].append({'nome': 'Ana', 'telefone': '21888888888', 'email': 'ana@gmail.com.br'})


# para fazer a gravação do processo
def criar_json():
    with open('clientes.json', 'w') as outfile:  # abrindo arquivo com arquivo externo
        json.dump(dados, outfile)


def testar_criar_json():
    criar_json()
    print(dados['cliente'])
