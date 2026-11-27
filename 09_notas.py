# Entgrada de dados
nome = input("Informe o nome: ").strip() .title()
nota1 = int(input("Informe a 1ª nota: "))
nota2 = int(input("Informe a 2ª nota: "))

# Processamento de dados
media = (nota1+nota2)/2

# Exibe a média
print(f"Média:{media}")

#  Estrutura de decisão
if media >= 7:
    print(f"{nome} Está aprovado! ")
elif media >=5:
    print(f"{nome} Está de recuperaçao! ")
else:
    print(f"Está reprovado! ")
    