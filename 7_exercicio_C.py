"""
7 - Dada uma lista de números A[1,2,3,…], faça um algoritmo que retorne uma lista somente
com os números pares.
"""

number = int(input('digite o número final para a lista: '))
lst = [n for n in range(number+1) if n % 2 == 0]
print('', 'Os números pares da lista são:', lst, sep='\n')
