"""
14 - Faça um algoritmo que recebe uma palavra e retorne se a palavra é palíndromo.
(Palavra que se pode ler, indiferentemente, da esquerda para direita ou vice-versa. Ex: osso,
Ana e etc)
"""

print(" Este programa verifica se a palavra é um PALÍNDROMO!")
palavra = input("Digite a palavra:").upper().replace(" ", "")
if palavra == palavra[::-1]:
    print("A palavra é um palíndromo")
else:
    print("A palavra não é um palíndromo")
