valor = int(input("Introduzca un numero: "))
print ("Usted debe pagar esto:", valor)
def calcular_descuento (valor, descuento_dado=20):
    descuento = valor * (descuento_dado/100)
    return descuento

descuento_final = calcular_descuento (valor)
print ("Su descuento es de:", descuento_final,"dolares aplicando el 20% de descuento")

res = (valor - descuento_final)
print ("Valor final a pagar aplicado su descuento del 20%:", res)