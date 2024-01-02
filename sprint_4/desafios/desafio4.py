def calcular_valor_maximo(operadores, operandos) -> float:
    if len(operadores) == len(operandos) and len(operadores) > 0:
        resultados = list(map(lambda args: eval(f"{args[0][0]}{args[1]}{args[0][1]}"), zip(operandos, operadores)))
    else:
        resultados = []

    return max(resultados, default=float('-inf'))
