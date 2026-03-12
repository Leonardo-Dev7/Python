multa = (5)
km_max = (80)

km = float(input("km/h: "))

if km >= 80:
    Valor = (km - km_max) * multa
    print("Acima da velocidade maxima!")
    print("Valor da multa para pagar: ", Valor)
else:
    print("Sem multas")