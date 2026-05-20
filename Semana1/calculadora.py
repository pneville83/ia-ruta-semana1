"""claculadora.py"""


NUMERO_1= int(input('Dame un numero'))
NUMERO_2= int(input('Dame otro numero'))

print ("el rssultado de la suma es:", NUMERO_1 + NUMERO_2)
print ("el resultado de la resta es: ", NUMERO_1 - NUMERO_2)
print("el resultado de la multiplicacion es: ", NUMERO_1 * NUMERO_2)

if NUMERO_2 != 0:
    print("el resultado de la division es: ", NUMERO_1 / NUMERO_2)
     
else:   
    print('la division entre cero no es posible')
    
