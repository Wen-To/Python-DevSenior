from datetime import datetime
import statistics

class Tarea:

    #funcion de iniciacilizacion = metodo constructor.
    def __init__(self, nombre, fechaLimite, categorias, horasDedicadas):
        self.nombre = nombre
        self.fechaLimite = fechaLimite
        self.categorias = categorias
        self.horasDedicadas = horasDedicadas

#Funcion para agregar una tarea
def agregarTarea(listaTareas):
    nombre = input("Ingrese el nombre de la tarea: ")
    fechaLimite_str = input("Ingrese la fehca limite de la tarea (DD/MM/YYYY): ")
    try:
        fechaLimite = datetime.strptime(fechaLimite_str, "%d/%m/%Y")
    except ValueError:
        print("Fecha no valida.")
        return
    categorias = input("Ingrese la categoria de la tarea (Estudio, Personal, Trabajo, Otras): ")
    horasDedicadas_str = input("Ingrese las horas dedicadas, separadas en comas: ")
    try:
        horasDedicadas = list(map(float, horasDedicadas_str.split(",")))
    except ValueError:
        print("Horas no validas.") 
        return
    #Crear un objeto y lo agrego a listas de tareas
    tarea = Tarea(nombre, fechaLimite, categorias, horasDedicadas)
    listaTareas.append(tarea)
    print("Tarea agregada con exito..")

def VisualizarTareas(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return
    for i, tarea in enumerate(listaTareas, start=1):
        print(f"\nTarea {i}")
        print(f"Nombre: {tarea.nombre}")
        print(f"Fecha limite: {tarea.fechaLimite.strftime('%d/%m/%Y')}")
        print(f"Categoria: {tarea.categorias}")
        print(f"Horas dedicadas: {tarea.horasDedicadas}")

def analizarHoras(listaTareas):
    if not listaTareas:
        print("No hay tareas registradas")
        return
    for tarea in listaTareas:
        promedio = statistics.mean(tarea.horasDedicadas)
        maximo = max(tarea.horasDedicadas)
        minimo = min(tarea.horasDedicadas)
        print(f"\nAnalisis de {tarea.nombre}")
        print(f"El promedio de horas: {promedio}")
        print(f"Maximo de horas: {maximo}")
        print(f"Minimo de horas {minimo}")
#Generar informe
def generarInforme(listaTareas):      
    if not listaTareas:
        print("No hay tareas")
        return
    
    #abrir un archivo txt para escribir un informe
    with open("Informe_tareas.txt", "w") as archivo:
        #escribir los detalles de la tarea en el archivo
        for tarea in listaTareas:
            archivo.write(f"Nombre: {tarea.nombre}\n")
            archivo.write(f"Fecha Limite {tarea.fechaLimite.strftime('%d/%m/%Y')}\n")
            archivo.write(f"Categorias: {tarea.categorias}\n")
            archivo.write(f"horasDedicadas: {tarea.horasDedicadas}\n")
            print("Informe generado como 'Informe_tareas.txt'")

def menu():
    listaTareas = []
    while True:
        print("\nMenu de opciones: ")
        print("1. Agregar tarea: ")
        print("2. Visualizar tareas: ")
        print("3. Analizar horas dedicadas: ")
        print("4. Generar informe: ")
        print("5. Salir ")
        




