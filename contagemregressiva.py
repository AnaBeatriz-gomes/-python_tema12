# Pede um número inteiro positivo ao usuário
x = int(input("Digite um número inteiro positivo: "))

# Contagem regressiva até 0
while x >= 0:
    print(x)
    x -= 1  # diminui 1 a cada repetição

print("Lançamento! Fim da contagem!")