# Função para encontrar o ator/atriz com mais filmes
def most_apearence_of_1_movie(file_path):
    count = 0
    lista_filmes = []
    contagem = {}

    # Abre o arquivo e itera sobre as linhas
    with open(file_path, 'r') as file:
        
        for line in file:
            # Tratamento de dados
            # Se a linha começar com aspas, separe por vírgula e remova as aspas
            if line[0].startswith('"'):
                line = line.split(',')
                line[0] = line[0].strip('"')
                # Correção do nome do ator
                line[0] = 'Robert Downey Jr.'
                # retirar coluna desnecessária
                if line[1] == ' Jr."':
                    line.pop(1)
            else:
                line = line.split(',')
            
            if line[4].startswith('1'):    
                line[4] = line[4].replace('1.8','')

            for i in range(len(line)):
                line[i] = line[i].strip()

            line[5] = line[5].strip(' \n')

            if count > 0:
                lista_filmes.append(line[4])

            count += 1
    
    for elemento in lista_filmes:
    # Se o elemento já está no dicionário, incremente sua contagem
        if elemento in contagem:
            contagem[elemento] += 1
        # Se o elemento não está no dicionário, adicione-o com uma contagem de 1
        else:
            contagem[elemento] = 1
    
    # Ordena o dicionário por valor
    contagem = dict(sorted(contagem.items(), key=lambda item: item[1], reverse=True))

    return contagem
    

file_path = 'actors.csv'
most_apearence = most_apearence_of_1_movie(file_path)

# Escreve o resultado em um arquivo de texto
with open('etapa-4.txt', 'w') as file:
    for index, key, value in zip(range(len(most_apearence)), most_apearence.keys(), most_apearence.values()):
        file.write(f"{index} - O filme {key} aparece {value} vez(es) no dataset\n")


