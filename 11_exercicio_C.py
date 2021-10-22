"""
11 - Dada duas lista de números A[1,2,3,4] e B[1,2,5,8], faça um algoritmo que retorne a
intersecção das listas
"""

a = [1, 2, 3, 4]
b = [1, 2, 5, 8]
c = list(set(a) & set(b))
print("A intersecção das listas é:", c)
