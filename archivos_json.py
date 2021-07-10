import json
#-CREAR UN OBJETO JSON A PARTIR DE UN STRING
contacto='{"Nombre":"Frank","Apellido":"Cipriano","edad":28}'
print(contacto)
print(type(contacto))
print('\n\n')

contacto_json=json.loads(contacto)
print(contacto_json)
print(type(contacto_json))
print(contacto_json["Nombre"])
print('\n\n')

#-CREAR UN OBJETO JSON A PARTIR DE UN DICCIONARIO
PERSONA={
    'Nombre':'Frank',
    'Apellido':'Cipriano',
    'edad':28,
    'Lenguajes':['Java','C++','Sql'],
    'tecnologias':{
        'backend':'nodejs',
        'frontend':['html','css']
    }
}

persona_json=json.dumps(PERSONA)
print(persona_json)
print(type(persona_json))
print(persona_json[2])
print('\n\n')

#-FORMATEANDO EL DATO JSON
persona_json=json.dumps(PERSONA,indent=4,separators=(",",":"))
print(persona_json)
print(type(persona_json))
print('\n\n')

#-ENCODER & DECODER
dato_json=json.JSONEncoder().encode({'Nombre':['Frank','Cipriano']})
print(dato_json)
print(type(dato_json))

dato_diccionario=json.JSONDecoder().decode(dato_json)
print(dato_diccionario)
print(type(dato_diccionario))
print('\n\n')

#-CREANDO UN JSON A PARTIR DE DATOS PLANOS OBTENIDOS EN UNA CLASE
class Json:
    def __init__(self,carrera,semestre):
        self.carrera=carrera
        self.semestre=semestre

carrera1 = Json('Sistemas','6to')
print(carrera1)
print(carrera1.carrera)
carrera_json=json.dumps(carrera1.__dict__)
print(carrera_json)
print(type(carrera_json))
carrera_dict=json.loads(carrera_json)
print(carrera_dict)
print(type(carrera_dict))
print(carrera_dict['carrera'])