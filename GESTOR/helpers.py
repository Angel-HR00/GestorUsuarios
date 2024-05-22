import re
import os
import platform

def clean_screen():
    #Limpia(vacia) la pantalla de la terminal
    os.system('cls') if platform.system() == "Windows" else os.system('clear')

def read_text(longitud_min = 0, longitud_max = 100, mensaje = None):
    print(mensaje) if mensaje else None
    
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto

def validate_dni(dni, lista):
    if not re.match('[0-9]{8}[A-Z]{1}$',dni):
        print("DNI no válido")
        return False
    for cliente in lista:
        if cliente.dni == dni:
            print("DNI usado por otro cliente")
            return False
    return True