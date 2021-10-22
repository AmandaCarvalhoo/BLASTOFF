# 8 - Faça um algoritmo que receba um número e retorne se o número é primo ou não.

def condprimo(i):
    fator = 2
    if i == 2:
        return True

    while i % fator != 0 and fator <= i/2:
        fator = fator + 1
    if i % fator <= 1:
        return False
    else:
        return True


n = int(input("Digite um número inteiro: "))


while n > 0:
    if condprimo(n):
        print("O número", n, "é primo")
    else:
        print("O número", n, "não é primo")
    n = int(input("Digite um número inteiro: "))
