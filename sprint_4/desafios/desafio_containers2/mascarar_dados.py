import hashlib

while True:

    # Receber uma string via input

    input_string = input("Digite uma palavra ou frase (ou 'exit' para sair): ")

    # Verificar se o usuário deseja sair

    if input_string.lower() == 'exit':

        break

    # Gerar o hash da string usando SHA-1

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()

    # Imprimir o hash em tela

    print(f"Hash SHA-1 da entrada '{input_string}': {sha1_hash}")

