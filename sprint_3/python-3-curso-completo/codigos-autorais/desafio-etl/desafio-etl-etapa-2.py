# Função para encontrar o ator/atriz com mais filmes
def media_of_gross(file_path):
    count = 0
    soma = 0

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
                # Soma os valores da coluna 5
                soma += float(line[5])
            count += 1
    
    return (soma/(count-1))
            

file_path = 'actors.csv'
media = media_of_gross(file_path)

with open('etapa-2.txt', 'w') as file:
    file.write(f'A media de faturamento é {media:.2f}')

