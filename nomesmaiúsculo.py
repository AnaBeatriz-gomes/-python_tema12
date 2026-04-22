#Passo 1 e 2: Lista vazia e leitura dos 5 nomes 
nomes = []

for i in range(5):
     nome = input(f"Digite o {i+1}º nome: ")
     nomes.append(nome)

#Passo 3: Exibir cada nome em maiúsculos 
print("\nNomes em maiúsculos:")
for nome in nomes:
     print(nome.upper())