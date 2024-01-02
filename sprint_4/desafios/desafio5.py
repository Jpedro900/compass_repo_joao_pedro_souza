import csv

# Ler o arquivo CSV
with open('estudantes.csv', 'r') as file:
    reader = csv.reader(file)

    # Processar os dados de cada estudante
    students = []
    for row in reader:
        # Verificar se a linha tem elementos suficientes
        if len(row) < 4:
            continue

        # Extrair o nome do estudante e as notas
        name = row[0]
        grades = list(map(int, row[1:]))

        # Ordenar as notas em ordem decrescente
        sorted_grades = sorted(grades, reverse=True)

        # Calcular a média das três maiores notas
        highest_grades = sorted_grades[:3]
        average = round(sum(highest_grades) / len(highest_grades), 2)

        # Gerar o relatório
        student_report = {
            'name': name,
            'grades': highest_grades,
            'average': average
        }
        students.append(student_report)

    # Ordenar os estudantes pelo nome
    students = sorted(students, key=lambda x: x['name'])

    # Imprimir o relatório para cada estudante
    for student in students:
        report = f"Nome: {student['name']} Notas: {student['grades']} Média: {student['average']}"
        print(report)
