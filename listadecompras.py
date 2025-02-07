"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista.
"""

# Importa o módulo 'os' para interagir com o sistema operacional (usado para limpar a tela)
import os

# Inicializa uma lista vazia para armazenar valores
lista = []

# Inicia um loop infinito para interação contínua com o usuário
while True:
    print('Selecione a opção: ')  # Exibe a mensagem para o usuário escolher uma ação
    # Solicita ao usuário que insira uma das opções: Inserir (I), Apagar (A) ou Listar (L)
    opção = input('[I]nserir, [A]pagar, [L]istar: ')

    # Se a opção for 'I' (Inserir), o código entra no primeiro bloco de código
    if opção == 'I':
        os.system('cls')  # Limpa a tela do terminal (Windows)
        valor = input('Valor: ')  # Solicita um valor ao usuário para ser inserido
        lista.append(valor)  # Adiciona o valor informado na lista

    # Se a opção for 'A' (Apagar), o código entra no segundo bloco de código
    elif opção == 'A':
        # Solicita o índice do item a ser apagado
        indice_str = input('Informe o índice: ')

        try:
            # Tenta converter o índice informado para um inteiro
            indice = int(indice_str)
            # Apaga o item da lista no índice especificado
            del lista[indice]

        except ValueError:
            # Se o índice não for um valor inteiro válido, exibe um erro
            print('Informe um valor inteiro válido.')
        except IndexError:
            # Se o índice estiver fora do alcance da lista, exibe um erro
            print('Este índice não existe.')
        except Exception:
            # Captura qualquer outro erro desconhecido
            print('Erro desconhecido.')

    # Se a opção for 'L' (Listar), o código entra no terceiro bloco de código
    elif opção == 'L':
        os.system('cls')  # Limpa a tela do terminal (Windows)

        # Verifica se a lista está vazia
        if lista == 0:
            print('Nada para listar')  # Exibe uma mensagem se a lista estiver vazia

        # Itera sobre os itens da lista e exibe cada valor com seu índice
        for i, valor in enumerate(lista):
            print(i, valor)

    # Caso a opção informada seja inválida, exibe uma mensagem de erro
    else:
        print('Informe a opção [I], [A] ou [L]')


