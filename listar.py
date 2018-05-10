#Crea un programa que muestre un listado de los titulos de los cines que tengan un id que empiecen por
#un numero que se le pedira al usuario por pantalla ademas tendra un acumulador que guardara el 
#numero de resultados.

import json

with open('salas-MADRID.json') as data_file:
    data = json.load(data_file)

# Nos pide un numero de referencia y coloca un contador
print(' ')
objeto=input('¿Porque numero empieza el id del cine que buscas?: ')
contador=0
print(' ')

for cine in (data['@graph']):
    comprobar=(cine['id'])
    if comprobar.startswith(objeto):
        contador=contador+1

print('Hay', contador, 'cine(s) que coinciden con la busqueda, espere a los resultados... ')
import time
time.sleep(3)
print('--------------------------------------------------------------------------------')
print(' ')
for cine in (data['@graph']):
    comprobar=(cine['id'])
    if comprobar.startswith(objeto):
        print(cine['title'])
print(' ')
print('--------------------------------------------------------------------------------')