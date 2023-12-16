#!/usr/local/bin/python3

with open('pessoas.csv') as arquivo: # with e um bloco de codigo que garante que o arquivo sera fechado, mesmo que ocorra algum erro durante a execucao do codigo.
    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo ja foi fechado.')
