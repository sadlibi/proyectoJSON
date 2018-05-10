#Programa que pide por teclado una localizacion y muestra todos los cines
#con esa localizacion, con su latitud y longitud y el id de su area.

import json

with open('salas-MADRID CORDOBA.json') as data_file:
    data = json.load(data_file)

locali=input('Dime una localizacion: ')

for sala in (data['@graph']):
    if (sala['address']['locality'])==locali:
        print('-------------------------------------------------------')
        print('Nombre:',sala['title'])
        print('Latitud: ', sala['location']['latitude'])
        print('Longitud: ', sala['location']['longitude'])
        print('Id de area:',sala['address']['area']["@id"])
        print(' ')
