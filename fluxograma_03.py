# Entrada de dados
nome = input("Digite seu nome: ").strip() .title()
idade = int(input("Digite sua idade: "))

# Saída de dados
if idade >= 18:
    print(f"{nome} É maior de idade!")
else:
    print(f"{nome} É menor de idade!")