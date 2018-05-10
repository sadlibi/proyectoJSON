#Crea un programa que muestre la descripcion del cine con su nombre, cuando este 
#situada en una calle y donde el nombre de esa calle se pida por teclado al usuario
#a modo de filtro. El programa comprobara que es una calle y que el nombre introducido
#por el usuario existe dentro de la cadena street-address. Si existe la calle se 
#mostrara por pantalla el resultado, si no se mostrara un mensaje de error.

import json

with open('salas-MADRID.json') as data_file:
    data = json.load(data_file)

print(' ')
nombrec=input('Dame el nombre de una calle para mostrar el cine: ')
print(' ')

contador=0
for sala in (data['@graph']):
    comprobarnombre=(sala['address']['street-address'])
    if comprobarnombre.startswith('CALLE'):
        if comprobarnombre.find(nombrec)!=-1:
            contador=contador+1
            print('-------------------------------------------------------')
            print('Nombre:', sala['title'])
            print(' ')
            print('Descripcion:', sala['organization']['organization-desc'])
            print('-------------------------------------------------------')
            print(' ')

if contador==0:
    print('No existe una calle con ese nombre')