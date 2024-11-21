conceptosProgramacion = {
    'POO' : 'Programacion Orientada a Objetos',
    'IDE' : 'Entorno de Desarrollo Integrado',
    'DBMS' : 'Sistema de Gestion de Bases de Datos'

}

print(conceptosProgramacion)
print(len(conceptosProgramacion))

print(conceptosProgramacion['IDE'])
print(conceptosProgramacion.get('POO'))

conceptosProgramacion['DBMS'] = 'Database Managment System'
print(conceptosProgramacion)
for key, value in conceptosProgramacion.items():
    print(key, value)