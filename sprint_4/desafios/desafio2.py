def conta_vogais(string):
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_presentes = list(filter(lambda x: x in vogais, string.lower()))
    return len(vogais_presentes)
