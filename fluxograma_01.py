# entrada de dados
nome = input ("Informe seu nome: ").strip().title()
email = input("Informe seu e-mail: ").strip().lower()
cpf = input("Informe seu CPF: ").strip()
telefone = input("Informe seu telefone: ").strip()
idade = int(input("Informe sua idade: "))
altura = float(input("Informe sua altura: ").replace(",","."))

# saída de dados
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"CPF: {cpf}")
print(f"Telefone: {telefone}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura} metros")