# Leia o arquivo e converta cada linha em um número inteiro
with open("numbers.txt", "r") as file:
    numbers = list(map(int, file.readlines()))

# Filtrar os números pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Ordenar os números pares em ordem decrescente
sorted_numbers = sorted(even_numbers, reverse=True)

# Imprimir os 5 maiores números pares
print(sorted_numbers[:5])

# Calcular a soma dos 5 maiores números pares
sum_of_numbers = sum(sorted_numbers[:5])

# Imprimir a soma
print(sum_of_numbers)
