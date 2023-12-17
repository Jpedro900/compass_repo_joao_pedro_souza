# Função para encontrar o ator/atriz com mais filmes
def actor_by_total_gross(file_path):
    count = 0
    lista_filmes = []

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
                lista_filmes.append((line[0], line[1]))

            count += 1

    lista_filmes = sorted(lista_filmes, key=lambda x: x[1], reverse=True)

    return lista_filmes
    

file_path = 'actors.csv'
actor = dict(actor_by_total_gross(file_path))

# Imprime o dicionário em sequência
with open('etapa-5.txt', 'w') as file:
    for key, value in actor.items():
        file.write(f"{key} - {value}\n")



