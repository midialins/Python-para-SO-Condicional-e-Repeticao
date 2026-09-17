x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

if x > y:
    diferenca = x - y
elif y > x:
    diferenca = y - x
else:
    diferenca = 0

print("A diferença é:", diferenca)
