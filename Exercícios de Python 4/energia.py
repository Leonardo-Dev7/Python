kWh = float(input("Quantos kWh foram usados: "))
tipo = input("Qual o tipo de Local (R para Residencial, C para Comercial ou I para Industrial): ").upper()

if tipo == 'R':
    if kWh <=500:
        Valor = kWh * 0.40
    else: 
        kWh >500
        Valor = kWh * 0.65

if tipo == 'C':
    if kWh <=1000:
        Valor = kWh * 0.55
    else: 
        kWh >1000
        Valor = kWh * 0.60
        
if tipo == 'I':
    if kWh <=5000:
        Valor = kWh * 0.55
    else:
        kWh >5000
        Valor = kWh * 0.60

print(f"O valor a ser pago é: R$ {Valor:.2f}")