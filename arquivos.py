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
        json.dump(dados, outfile, indent=4)
    with open('clientes2.json', 'w') as outfile:  # abrindo arquivo com arquivo externo
        json.dump(dados, outfile, indent=4)
    with open('clientes3.json', 'w') as outfile:  # abrindo arquivo com arquivo externo
        json.dump(dados, outfile, indent=4)

def ler_e_adicionar_json():
    with open('clientes2.json') as outfile:
        dados2 = json.load(outfile)
        temp = []
        for registro in dados2['cliente']:
            print('nome:' + registro['nome'])
            print('telefone:' + registro['telefone'])
            print('email:' + registro['email'])
            print('')


            # Salvar na lista
            temp.append(
                '\'nome\'' + ':' + '\'' + registro['nome'] + '\',' \
                + '\'telefone\'' + ':' + '\'' + registro['telefone'] + '\',' \
                + '\'email\'' + ':' + '\'' + registro['email'] + '\''
            )

        dados['cliente'].extend(temp)


def ler_json():
    with open('clientes2.json') as outfile:
        dados = json.load(outfile)
        for registro in dados['cliente']:
            print('nome:' + registro['nome'])
            print('telefone:' + registro['telefone'])
            print('email:' + registro['email'])
            print('')


def testar_criar_json():
    criar_json()
    print(dados['cliente'])


def testar_ler_json():
    print('Leitura de Json por linha / campo')
    ler_json()
    print(dados['cliente'])


def testar_ler_e_adicionar_json():
    ler_e_adicionar_json()
    print('Lista atualizada final')
    print(dados['cliente'])
