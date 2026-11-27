# Entrada de dados
massa = float(input("Informe a massa muscular: ").replace(",","."))
altura = float(input("Informe a altura: ").replace(",","."))

if massa <= 140 and altura >= 1.15:
    print(f"Entrada do usuário permitida.")
else:
    print(f"Entrada do usuário negada.")