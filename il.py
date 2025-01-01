# librerias 
import speech_recognition as sr
import pyttsx3
import random
import matplotlib.pyplot as plt
plt.ion()  # Turn on interactive mode 
#definir la clase
class RegistroNombres:
    def __init__(self): 
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.7)

        self.nombres = []
        self.apellidos_paternos = []
        self.apellidos_maternos = []

    def hablar(self, texto):
        """Método para que el asistente hable"""
        self.engine.say(texto)
        self.engine.runAndWait()
#Metodo escuchar
    def escuchar(self, mensaje_inicial, lista_actual):
        """Método para escuchar y registrar un nombre o apellido directamente"""
        while len(lista_actual) < 20: 
            try:
                with sr.Microphone() as source:
                    self.hablar(mensaje_inicial + f" {len(lista_actual) + 1} de 20")
                    print(f"Escuchando {mensaje_inicial.lower()}...")

                    audio = self.listener.listen(source)
                    texto = self.listener.recognize_google(audio, language='es-ES').lower()

                    lista_actual.append(texto)
                    self.hablar(f"{mensaje_inicial} registrado: {texto}")

            except sr.UnknownValueError:
                self.hablar("No te escuché bien, intenta de nuevo")
            except sr.RequestError:
                self.hablar("Hubo un problema con el servicio de reconocimiento de voz")
#Metodo registrar
    def registrar_datos(self):
        """Método principal para registrar nombres y apellidos"""
        self.hablar("Vamos a registrar 20 nombres, 20 apellidos paternos y 20 apellidos maternos")

        self.escuchar("Nombre", self.nombres)

        self.escuchar("Apellido Paterno", self.apellidos_paternos)

        self.escuchar("Apellido Materno", self.apellidos_maternos)

        self.hablar("Registro completado. Mostraré los resultados.")
        print("\n--- RESULTADOS DEL REGISTRO ---")
        for i in range(20):
            print(f"{i+1}. {self.nombres[i]} {self.apellidos_paternos[i]} {self.apellidos_maternos[i]}")
#Seccion para generar tuplas
    def generar_tuplas(self):
        """Genera 10,000 tuplas con ID, Edad, Peso y Localidad"""
        localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
        tuplas = []

        for i in range(10000):
            nombre = random.choice(self.nombres)
            apellido_paterno = random.choice(self.apellidos_paternos)
            apellido_materno = random.choice(self.apellidos_maternos)
            edad = random.randint(1, 100)  
            peso = random.uniform(1.0, 100.0)  
            localidad = random.choice(localidades)
            id_persona = f"ID-{i+1:05}"  # IDs como ID-00001, ID-00002, etc.

            tupla = (id_persona, f"{nombre} {apellido_paterno} {apellido_materno}", edad, round(peso, 2), localidad)
            tuplas.append(tupla)

        return tuplas

#preguntas ¿Cuántos hermanos hay en la Base de Datos?

def contar_hermanos(tuplas):
    contador = 0
    grupos_hermanos = {}

    for tupla in tuplas:

        apellido_paterno = tupla[2]
        apellido_materno = tupla[3]
        nombre_completo = tupla[1]

        clave = (apellido_paterno, apellido_materno)
    
        if clave not in grupos_hermanos:
            grupos_hermanos[clave] = []

        grupos_hermanos[clave].append(nombre_completo)

    for grupo, nombres in grupos_hermanos.items():
        if len(nombres) > 1:
            contador += len(nombres)  

    return contador


#¿Cuántos homónimos hay en la Base de Datos?
def contar_homonimos(tuplas):
    contador = 0
    grupos_homonimos = {}

    for tupla in tuplas:
        nombre_completo = tupla[1]

        if nombre_completo not in grupos_homonimos:
            grupos_homonimos[nombre_completo] = []

        grupos_homonimos[nombre_completo].append(tupla)

    for grupo, personas in grupos_homonimos.items():
        if len(personas) > 1:
            contador += 1

    return contador

#Genere el histograma de edades (total y por localidad--5)
def generar_histograma_edades(tuplas):
    edades = [tupla[2] for tupla in tuplas] #extraídas de la tercera posición
    
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    edades_por_localidad = {localidad: [] for localidad in localidades} #diccionario y se llenarán con las edades

    for tupla in tuplas:
        localidad = tupla[4]
        edad = tupla[2]
        if localidad in edades_por_localidad:
            edades_por_localidad[localidad].append(edad)
    
    # Primera figura- Total and all localidades combined
    plt.figure(figsize=(10, 6))
    plt.hist(edades, bins=20, alpha=0.5, label="Total", color='blue')

    for localidad, edades_localidad in edades_por_localidad.items():
        plt.hist(edades_localidad, bins=20, alpha=0.5, label=localidad, edgecolor='black')
    plt.title("Histograma de Edades (Total y por Localidad)")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.legend(loc="upper right")
    plt.grid(True)
    
    # Segunda figura - para cada localidad
    plt.figure(figsize=(15, 10))
    for i, localidad in enumerate(localidades, 1):
        plt.subplot(2, 3, i)
        plt.hist(edades_por_localidad[localidad], bins=20, alpha=0.5, label=localidad, edgecolor='black')
        plt.title(f"Histograma de Edades ({localidad})")
        plt.xlabel("Edad")
        plt.ylabel("Frecuencia")
        plt.legend(loc="upper right")
        plt.grid(True)
    plt.tight_layout()
    
    # Mostrar las figuras
    plt.show(block=True)

def generar_histograma_peso(tuplas):
    pesos = [tupla[3] for tupla in tuplas]
    
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    pesos_por_localidad = {localidad: [] for localidad in localidades}

    for tupla in tuplas:
        localidad = tupla[4]  
        peso = tupla[3]       
        if localidad in pesos_por_localidad:
            pesos_por_localidad[localidad].append(peso)
    
    # Primera figura 
    plt.figure(figsize=(10, 6))
    plt.hist(pesos, bins=20, alpha=0.5, label="Total", color='green')

    for localidad, pesos_localidad in pesos_por_localidad.items():
        plt.hist(pesos_localidad, bins=20, alpha=0.5, label=localidad, edgecolor='black')
    
    plt.title("Histograma de Pesos (Total y por Localidad)")
    plt.xlabel("Peso (kg)")
    plt.ylabel("Frecuencia")
    plt.legend(loc="upper right")
    plt.grid(True)

    # Segunda figura
    plt.figure(figsize=(15, 10))
    for i, localidad in enumerate(localidades, 1):
        plt.subplot(2, 3, i)
        plt.hist(pesos_por_localidad[localidad], bins=20, alpha=0.5, label=localidad, edgecolor='black')
        plt.title(f"Histograma de Pesos ({localidad})")
        plt.xlabel("Peso (kg)")
        plt.ylabel("Frecuencia")
        plt.legend(loc="upper right")
        plt.grid(True)
    
    plt.tight_layout()
    
    # Mostrar las figuras
    plt.show(block=True)

#¿Qué localidad tiene mayor porcentaje de menores (<18)?
def localidad_mayor_porcentaje_menores(tuplas):
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    porcentajes = []

    for localidad in localidades: 

        personas_localidad = [tupla for tupla in tuplas if tupla[4] == localidad] 
        
        menores = sum(tupla[2] < 18 for tupla in personas_localidad)
        #calculo del porcentaje
        if len(personas_localidad) > 0:
            porcentaje = menores / len(personas_localidad) * 100
        else:
            porcentaje = 0  
        
        porcentajes.append(porcentaje)
  
    localidad_mayor_porcentaje = localidades[porcentajes.index(max(porcentajes))]

    return localidad_mayor_porcentaje

#¿Qué localidad tiene mayor porcentaje de adultos (18-60)?
def localidad_mayor_porcentaje_adultos(tuplas):
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    porcentajes = []

    for localidad in localidades:

        personas_localidad = [tupla for tupla in tuplas if tupla[4] == localidad]
        
        adultos = sum(18 <= tupla[2] <= 60 for tupla in personas_localidad)
        
        if len(personas_localidad) > 0:
            porcentaje = adultos / len(personas_localidad) * 100
        else:
            porcentaje = 0  
        
        porcentajes.append(porcentaje)
  
    localidad_mayor_porcentaje = localidades[porcentajes.index(max(porcentajes))]

    return localidad_mayor_porcentaje

#¿Qué localidad tiene mayor porcentaje de mayores (>60)?
def localidad_mayor_porcentaje_mayores(tuplas):
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    porcentajes = []

    for localidad in localidades:

        personas_localidad = [tupla for tupla in tuplas if tupla[4] == localidad]
        
        mayores = sum(tupla[2] > 60 for tupla in personas_localidad)
        
        if len(personas_localidad) > 0:
            porcentaje = mayores / len(personas_localidad) * 100
        else:
            porcentaje = 0  
        
        porcentajes.append(porcentaje)
  
    localidad_mayor_porcentaje = localidades[porcentajes.index(max(porcentajes))]

    return localidad_mayor_porcentaje

#¿En qué localidad son más pesados los adultos (18-60)?
def localidad_mas_pesados_adultos(tuplas):
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    pesos_adultos_por_localidad = {localidad: [] for localidad in localidades}

    for tupla in tuplas:#recorremos la tupla
        localidad = tupla[4]
        edad = tupla[2]
        peso = tupla[3]
        if 18 <= edad <= 60:  
            if localidad in pesos_adultos_por_localidad:
                pesos_adultos_por_localidad[localidad].append(peso)
    # Calcular el promedio de pesos para cada localidad
    promedios_pesos = {localidad: sum(pesos_adultos_por_localidad[localidad]) / len(pesos_adultos_por_localidad[localidad]) 
                       if len(pesos_adultos_por_localidad[localidad]) > 0 else 0 
                       for localidad in pesos_adultos_por_localidad}

    localidad_mas_pesados = max(promedios_pesos, key=promedios_pesos.get) 

    return localidad_mas_pesados

#¿Cuál es la localidad más longeva?
def localidad_mas_longeva(tuplas):
    localidades = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    edades_maximas_por_localidad = {}

    for localidad in localidades:
        personas_localidad = [tupla for tupla in tuplas if tupla[4] == localidad]
        if personas_localidad:  # Check if the list is not empty
            max_edad = max(tupla[2] for tupla in personas_localidad)  # Edad máxima de esa localidad
            edades_maximas_por_localidad[localidad] = max_edad
        else:
            edades_maximas_por_localidad[localidad] = 0

    localidad_mas_longeva = max(edades_maximas_por_localidad, key=edades_maximas_por_localidad.get)

    return localidad_mas_longeva
#funcion principal
def main(): #organiza la ejecucion del programa
    registro = RegistroNombres()
    registro.registrar_datos()

    datos = registro.generar_tuplas()

    print("\n--- TODAS LAS TUPLAS GENERADAS ---")
    for tupla in datos[:10]:  
        print(tupla)
    
    # Llamar a las funciones
    cantidad_hermanos = contar_hermanos(datos)
    print(f"\nLa cantidad total de hermanos en la base de datos es: {cantidad_hermanos}")
    
    cantidad_homonimos = contar_homonimos(datos)
    print(f"\nLa cantidad total de homónimos en la base de datos es: {cantidad_homonimos}")
    
    localidad_menores = localidad_mayor_porcentaje_menores(datos)
    print(f"\nLa localidad con mayor porcentaje de menores (<18): {localidad_menores}")

    localidad_adultos = localidad_mayor_porcentaje_adultos(datos)
    print(f"La localidad con mayor porcentaje de adultos (18-60): {localidad_adultos}")

    localidad_mayores = localidad_mayor_porcentaje_mayores(datos)
    print(f"La localidad con mayor porcentaje de mayores (>60): {localidad_mayores}")

    localidad_mas_pesados = localidad_mas_pesados_adultos(datos)
    print(f"La localidad con los adultos más pesados: {localidad_mas_pesados}")

    localidad_mas_longeva_max = localidad_mas_longeva(datos)
    print(f"La localidad más longeva: {localidad_mas_longeva_max}")

    # Generar histogramas (esto abrirá ventanas con los gráficos)
    generar_histograma_edades(datos)
    generar_histograma_peso(datos)

if __name__ == "__main__": #ayuda a ejecutar el programa una vez se regitran los datos
    main()