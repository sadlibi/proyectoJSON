#Imagina que tenemos descuentos en la salas donde la entidad u organismos 'CinesFilmoteca'
#esta implicada. Bien queremos saber cuales son los cines de MADRID donde tenemos descuento,
#vamos en coche y la accesibilidad tiene que ser pequeña porque nuestro coche no es muy grande. 
#Nos hemos montado en el coche pero nos hemos dado cuenta que no tenemos gasolina para mucho
#asi que queremos que este en un barrio del distrito Arganzuela.
#El programa ademas mostrara todos los barrios de Arganzuela donde hay cines y pedira al 
#usuario que seleccione el cine para mostrarle la localizacion mediante la latitud y la
#longitud.

#Filtrar por CinesFilmoteca.
#Filtrar por accesibilidad 0.
#Filtrar por distrito Arganzuela.
#Dar la opcion de seleccionar el cine para dar la localizacion (lat/long).

#Todo debe ser interactivo(Pregunta respuesta) pero en el caso de introducir todos los requisitos anteriores 
#deben salir 2 cines: Cine Artistic Metropol y Cine Cinesa Mendez Alvaro 3D y se podra elegir uno.

import json

with open('salas-MADRID CORDOBA.json') as data_file:
    data = json.load(data_file)

    
lista=[]
tipopregunta=input('¿Que tipo de cine quieres?: ')
accesopregunta=input('¿Que tipo de accesibilidad necesita?[Grande=1 Pequeña=0 Sin=""]: ')
distritopregunta=input('¿En que distrito quiere que este?: ')
print(' ')

for sala in (data['@graph']):
    tipo=(sala['@type'])
    acceso=(sala['organization']['accesibility'])
    distrito=(sala['address']['area']['@id'])
    nombre=(sala['title'])
    if tipo.find(tipopregunta)!=-1 and acceso.find(accesopregunta)!=-1 and distrito.find('Arganzuela')!=-1:
        lista.append(nombre)

print('Estas son las opciones: ') 
print(' ')
for cine in lista:
    import time
    time.sleep(1)
    print('-',cine)

print(' ')
opcion=input('¿A que cine quieres ir?: ')    
print(' ')
for sala2 in (data['@graph']):
    nombre2=(sala2['title'])
    if nombre2==opcion:
        latitud=(sala2['location']['latitude'])
        longitud=(sala2['location']['longitude'])
        direct=(sala2['address']['street-address'])
        print('Direccion:',direct)
        print('Latitud:',latitud)
        print('Longitud:',longitud)
        