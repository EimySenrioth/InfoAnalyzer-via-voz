import speech_recognition as sr
import pyttsx3
import random

class RegistroNombres:
    def __init__(self):
        self.listener = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.7)

        # Listas para almacenar los registros
        self.nombres = []
        self.apellidos_paternos = []
        self.apellidos_maternos = []

    def hablar(self, texto):
        """Método para que el asistente hable"""
        self.engine.say(texto)
        self.engine.runAndWait()

    def escuchar(self, mensaje_inicial, lista_actual):
        """Método para escuchar y registrar un nombre o apellido"""
        while len(lista_actual) < 20:
            try:
                with sr.Microphone() as source:
                    self.hablar(mensaje_inicial + f" {len(lista_actual) + 1} de 20")
                    print(f"Escuchando {mensaje_inicial.lower()}...")

                    audio = self.listener.listen(source)
                    texto = self.listener.recognize_google(audio, language='es-ES').lower()

                    self.hablar(f"¿Confirmaste {texto}? Di 'sí' o 'no'")

                    confirmacion = self.listener.listen(source)
                    confirmacion_texto = self.listener.recognize_google(confirmacion, language='es-ES').lower()

                    if 'sí' in confirmacion_texto:
                        lista_actual.append(texto)
                        self.hablar(f"{mensaje_inicial} registrado: {texto}")
                    else:
                        self.hablar("Registro cancelado, intenta de nuevo")

            except sr.UnknownValueError:
                self.hablar("No te escuché bien, intenta de nuevo")
            except sr.RequestError:
                self.hablar("Hubo un problema con el servicio de reconocimiento de voz")

    def registrar_datos(self):
        """Método principal para registrar nombres y apellidos"""
        self.hablar("Vamos a registrar 20 nombres, 20 apellidos paternos y 20 apellidos maternos")

        # Registrar nombres
        self.escuchar("Nombre", self.nombres)

        # Registrar apellidos paternos
        self.escuchar("Apellido Paterno", self.apellidos_paternos)

        # Registrar apellidos maternos
        self.escuchar("Apellido Materno", self.apellidos_maternos)

        # Mostrar resultados
        self.hablar("Registro completado. Mostraré los resultados.")
        print("\n--- RESULTADOS DEL REGISTRO ---")
        for i in range(20):
            print(f"{i+1}. {self.nombres[i]} {self.apellidos_paternos[i]} {self.apellidos_maternos[i]}")

def main():
    registro = RegistroNombres()
    registro.registrar_datos()

if __name__ == "__main__":
    main()

#tuplas

def generar_tupla(self):
    """Método para generar una tupla aleatoria con ID, Edad, Peso, Localidad"""
    localidad = ["Barcelona", "Madrid", "Sevilla", "Valencia", "Zaragoza"]
    tuplas = []
    
    for i in range(10000):
        nombre = random.choice(self.nombres)
        apellido_paterno = random.choice(self.apellidos_paternos)
        apellido_materno = random.choice(self.apellidos_maternos)
        edad = random.randint(1, 100)
        peso = random.uniform(1.0, 100.0)
        localidad = random.choice(localidad)
        id = f"ID-{i+1:05}"
        
        tupla = (id, f"{nombre} {apellido_paterno} {apellido_materno}", edad, round(peso, 2), localidad)
        tuplas.append(tupla)
    
    return tuplas

    def main():
        registro = RegistroNombres()
        registro.registrar_datos()

        datos = generar_tupla(registro)

        print("\n--- EJEMPLO DE TUPLAS GENERADAS ---")
        for tupla in datos[:10]:
            print(tupla)

if __name__ == "__main__":
    main()