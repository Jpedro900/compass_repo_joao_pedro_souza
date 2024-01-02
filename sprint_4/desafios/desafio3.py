from functools import reduce

def calcula_saldo(lancamentos):
    valores = map(lambda x: x[0], lancamentos)
    tipos = map(lambda x: x[1], lancamentos)
    
    saldo = reduce(lambda acc, x: acc + x if tipos.__next__() == 'C' else acc - x, valores, 0)
    return saldo

lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]

saldo_final = calcula_saldo(lancamentos)
print(saldo_final)
