"""Gerar senha aleatória"""

import random
from rest_framework.decorators import api_view
from rest_framework.response import Response


def verifica_dict(**kwargs):
    """Retorna todos as chaves que contém o valor False"""
    # se não tiver nada retorna NONE
    falsos = [k for k, v in kwargs.items() if v == False]
    return falsos


def remover_chaves(lista, **kwargs):
    """Remove todas as chaves indesejadas, do dicionário"""
    if lista:
        for chave in lista:
            kwargs.pop(chave, "Chave não encontrada!")
    return kwargs


@api_view(["POST"])
def gerar_senha(**json):  # recebe o json
    """Gera a senha de acordo com os tipos de caracteres informados"""
    senha = {  # opções de caracteres
        "numeros": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],

        "simbolos": [
            "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", ":", "+",
            "[", "]", "{", "}", "\\", "|", ";", ":", "'", '"', ",", "<", ".", ">", "/", "?"
        ],

        "letras_minusculas": [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        ],

        "letras_maiusculas": [
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        ]
    }

    a = verifica_dict(**json)

    # obtendo o valor da quantidade de caracteres
    qtd_caracteres = json.get('qtd_caracteres')

    # se tiver(em) iten(s), o(s) remove
    if a:
        nova_senha = remover_chaves(a, **senha)
        senha = nova_senha

    # cria lista com os valores possíveis
    soma_lista = []
    for value in senha.values():
        soma_lista += value

    # preenche a lista com os values até chegar no máximo de qtd_caracteres
    try:
        soma_lista = random.choices(soma_lista, k=qtd_caracteres)
        random.shuffle(soma_lista)  # embaralha a lista
        senha_string = ''.join(soma_lista)  # forma final da senha
    except IndexError:
        return Response("Nenhuma senha foi gerada, pois nenhuma característica foi selecionada.")
    # retornar Http Response para o React
    return Response({"senha_gerada": senha_string})
