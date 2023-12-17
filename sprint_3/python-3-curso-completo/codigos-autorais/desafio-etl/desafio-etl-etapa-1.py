# Função para encontrar o ator/atriz com mais filmes
def find_actor_with_most_movies(file_path):
    max_movies = 0
    actor_with_most_movies = ""
    count = 0

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
            
            # Retirar espaços em branco e quebra de linha
            for i in range(len(line)):
                line[i] = line[i].strip()

            line[5] = line[5].strip(' \n')

            
            
            if count > 0:
            # Se o número de filmes for maior que o máximo atual, atualiza o máximo e o nome do ator/atriz
                if int(line[2]) > max_movies:
                    max_movies = int(line[2])
                    actor_with_most_movies = line[0]
            count += 1
    
    return actor_with_most_movies, max_movies
            

file_path = 'actors.csv'
actor,movies = find_actor_with_most_movies(file_path)

with open('etapa-1.txt', 'w') as file:
    file.write(f'O ator/atriz com mais filmes é {actor} com {movies} filmes')

