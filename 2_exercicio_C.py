import numpy as np

"""
 2- Dada a distância A e o combustível gasto B, faça um algoritmo
 para calcular o consumo médio.

"""
print("Este programa calcula a média de consumo do automóvel,\nInsira somente números para efetuar um cálculo!")
a = float(input("Digite a distância em Km percorrida: "))
b = float(input("Quantos litros de combustível foi consumido? "))
consumo = float(a) / float(b)
print("O consumo médio em litros foi de:", float(np.round(consumo)), 'L')
