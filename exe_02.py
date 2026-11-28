# TODO: Crie um programa que receba do usuário o nome, a massa
# e a altura, calcule seu IMC (Índice de Massa Corporal).
# Após mostrar o IMV, o programa deve informar de acordo com o 
# valor do seu IMC:
# - IMC < 18.5: "Usuário está abaixo do peso ideal"
# - IMC < 25: "Usuário está no peso ideal"
# - IMC < 30: "Usuário está acima do peso"
# - IMC < 35: "Usuário está obeso"
# - IMC < 40: "Usuário está com obesidade nível 2"
# - Se não estiver em nenhum dos casos acima:
# - "Usuário está com obesidade mórbida"


# Entrada de dados

nome = input("Digite seu nome: ")
massa = float(input("Digite sua massa (kg): ").replace(",","."))
altura = float(input("Digite sua altura (m): ").replace(",", "."))

# Prcessamento
imc = massa / (altura ** 2)

# Saídade de dados
print(f"IMC: {imc:.2f}")

if imc < 18.5:
    print(f"{nome}, você está abaixo do peso ideal.")
elif imc < 25:
    print(f"{nome}, você está no peso ideal.")
elif imc < 30:
    print(f"{nome}, você está acima do peso.")
elif imc < 35:
    print(f"{nome}, você está obeso.")
elif imc < 40:
    print(f"{nome}, você está com obesidade nível 2.")
else:
    print(f"{nome}, você está com obesidade mórbida.")
