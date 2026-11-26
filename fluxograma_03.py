# Entrada de dados
nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))

# Saída de dados
if idade >= 18:
    print(f"{nome} É maior de idade!")
else:
    print(f"{nome} É menor de idade!")