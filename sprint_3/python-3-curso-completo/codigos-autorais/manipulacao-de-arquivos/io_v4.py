#!/usr/local/bin/python3

try: # try/finally e um bloco de codigo que garante que o arquivo sera fechado, mesmo que ocorra algum erro durante a execucao do codigo.
    arquivo = open('pessoas.csv')

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except IndexError:
    pass
finally:
    arquivo.close()

if arquivo.closed:
    print('Arquivo ja foi fechado.')
