numero = int(input("Digite um numero inteiro:"))

divisores = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores = divisores + 1

if numero > 1 and divisores == 2:
    print("O numero e primo")
else:
    print("O numero nao e primo")
