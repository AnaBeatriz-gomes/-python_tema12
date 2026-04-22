# Pergunta quantas notas o usuário quer digitar
quantidade = int(input("Quantas notas deseja digitar? "))

soma = 0

# Loop para ler cada nota
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota

# Calcula a média
media = soma / quantidade

# Exibe a média com 2 casas decimais
print(f"Média final: {media:.2f}")

# Verifica situação do aluno
if media >= 7:
    print("APROVADO!")
else:
    print("REPROVADO!")