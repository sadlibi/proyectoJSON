#Crea un programa que cuente el numero de veces donde la accesibilidad de la organizacion
#es 1 tomandolo como accesible, 0 tomandolo como no accesible o "" tomandolo como nulo y 
#muestre por pantalla el resultado.

import json

with open('salas-MADRID.json') as data_file:
    data = json.load(data_file)

accesibles=0
nonaccesibles=0
nulas=0
for sala in (data['@graph']):
    acceso=(sala['organization']['accesibility'])
    if acceso=='1':
        accesibles=accesibles+1
    elif acceso=='0':
        nonaccesibles=nonaccesibles+1
    else:
        nulas=nulas+1

print('El numero total de organizaciones accesibles son:', accesibles)
print('El numero total de organizaciones no accesibles son:', nonaccesibles)
print('El numero total de organizaciones con acceso nulo son:', nulas)