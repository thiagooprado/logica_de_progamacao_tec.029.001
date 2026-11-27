# TODO: Crie um programa que receba do usuário o valor da gasolina
# e do etanol, e informe para o usuário qual o melhor combustível
# para abastecer.
# NOTE: Compensa mais abastecer com etanol caso o valor do etanol
# corresponda a até 75% do valor da gasolina.
# NOTE: E não se esqueça do detalhe mais importante de todos:
# DIVIRTAM-SE!!!


gasolina = float(input("Digite o valor da gasolina: ").replace(",","."))
etanol = float(input("Digite o valor do etanol: ").replace(",","."))

if etanol <= gasolina * 0.75:
    print("Compensa abastecer com etanol!")
else:
    print("Compensa abastecer com gasolina!")
