# 5 - Faça um algoritmo para apresentar se dois números são múltiplos.

# Obs: entendi que é para calcular se um número é multiplo do outro

num1 = int(input('Digite o primeiro número para verificar se é multiplo: '))

num2 = int(input('Digite o segundo número para verificar se é multiplo: '))

calc = num1 / num2
if num1 % num2 == 0:
    print("Os números {} e {} São multiplos!".format(num1, num2))
else:
    print("Os números {} e {} Não são multiplos!".format(num1, num2))
