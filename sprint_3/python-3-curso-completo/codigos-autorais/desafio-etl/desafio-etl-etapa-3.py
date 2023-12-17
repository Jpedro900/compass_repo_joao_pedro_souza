# Função para encontrar o ator/atriz com mais filmes
def actor_with_most_gain_per_movie(file_path):
    count = 0
    most_gain_per_movie = 0
    actor = ''

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
            
            for i in range(len(line)):
                line[i] = line[i].strip()
            
            if line[4].startswith('1'):    
                line[4] = line[4].replace('1.8','')

            line[5] = line[5].strip(' \n')
            
            if count > 0:
                # Mostra o ator com maior faturamento por filme
                if float(line[3]) > most_gain_per_movie:
                    most_gain_per_movie = float(line[3])
                    actor = line[0]
            count += 1
    
    return actor
            

file_path = 'actors.csv'
actor = actor_with_most_gain_per_movie(file_path)

# Escreve o resultado em um arquivo de texto
with open('etapa-3.txt', 'w') as file:
    file.write(f'O ator com maior faturamento por filme é {actor}')
