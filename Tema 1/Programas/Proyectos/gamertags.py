def header():
    """Muestra la cabecera del proyecto"""
    title = r""" 
                                                                                                    
    ▄▄▄▄                                          ▄▄▄▄▄▄▄▄                               
  ██▀▀▀▀█                                         ▀▀▀██▀▀▀                               
 ██         ▄█████▄  ████▄██▄   ▄████▄    ██▄███     ██      ▄█████▄   ▄███▄██  ▄▄█████▄ 
 ██  ▄▄▄▄   ▀ ▄▄▄██  ██ ██ ██  ██▄▄▄▄██   ██▀        ██      ▀ ▄▄▄██  ██▀  ▀██  ██▄▄▄▄ ▀ 
 ██  ▀▀██  ▄██▀▀▀██  ██ ██ ██  ██▀▀▀▀▀▀   ██         ██     ▄██▀▀▀██  ██    ██   ▀▀▀▀██▄ 
  ██▄▄▄██  ██▄▄▄███  ██ ██ ██  ▀██▄▄▄▄█   ██         ██     ██▄▄▄███  ▀██▄▄███  █▄▄▄▄▄██ 
    ▀▀▀▀    ▀▀▀▀ ▀▀  ▀▀ ▀▀ ▀▀    ▀▀▀▀▀    ▀▀         ▀▀      ▀▀▀▀ ▀▀   ▄▀▀▀ ██   ▀▀▀▀▀▀  
                                                                       ▀████▀▀           
                                                                                                       
                                🎮¡Crea tu Identidad Gamer!🎮                               """
    print(title)

def create_basic_tag(name):
    """
    Crea un gamerTag Basico usando las primeras 4 letras del nombre
    Parámetros:
    name(String) : Nombre del usuario
    Retorna:
    str: GamerTag Básico
    """
    tag = name[0:4]
    return tag

def create_invert_tag(name):
    """
    Crea un gamerTag invirtiendo el nombre completo 
    Párametro:
    str: Nombre del usuario
    Retorna:
    str: gamerTagInvertido
    """
    tag = name[::-1]
    return tag

def create_intespersed_tag (name,lastname):
    """
    Crea un gamerTag intercalando el nombre y apellido
    Parametro:
    str: Nombre 
    str: Apellido
    Retorna:
    str: gamerTagIntercalado
    """
    tag = f"{name[0]}{lastname[0]}{name[1:]}{lastname[1:]}"
    return tag

def create_elite_tag (name):
    """
    Crea un gamerTag elite a partir del nombre
    Parametro:
    str: Nombre 
    Retorna:
    str: gamerTagElite
    """
    tag = f"{name[0:2]}{name[-2:]}"
    return tag

def create_Number_tag(name,FNumber):
     """
    Crea un gamerTag elite a partir del nombre y el numero favorito
    Parametro:
    str: Nombre 
    int: Numero Favorito
    Retorna:
    str: gamerTagNumero
    """
     tag = f"{name[:5]}{fNumber}"
     return tag

def show_statistics(name):
    print("\n==================================")
    print("📊 ESTADÍSTICAS DE TU NOMBRE:")
    print("==================================")
    print(f"Nombre Completo: {name}")
    print(f"Longitud del nombre: {len(name)}")
    print(f"Primera letra: {name[0]}")
    print(f"Ultima letra: {name[-1]}")
    return

def create_tagNames (name,lastName,fNumber):
    print("\n==================================")
    print(f"🎯TUS OPCIONES DE GAMERTAG")
    print("==================================")
    print(f"TAG BASICO: {create_basic_tag(name)}")
    print(f"TAG INVERTIDO: {create_invert_tag(name)}")
    print(f"TAG INTERCALADO: {create_intespersed_tag(name,lastName)}")
    print(f"TAG ELITE: {create_elite_tag(name)}")
    print(f"TAG CON NUMERO: {create_Number_tag(name,fNumber)}")
    return


#Función que define el encabezado del programa 
header()
#Inputs para ingresar el nombre, apellido y numero favorito
name = input("\nIntroduce tu nombre: ")
lastName = input("Introduce tu apellido: ")
fNumber= input("Introduce tu numero favorito: ")
#Función que mostrará las estadisticas 
show_statistics(name)
#Función que manda a llamar las funciones que generan los diferentes tipos de tags
create_tagNames(name,lastName,fNumber)

print("\n ✨ Elige tu favorito y conquista el mundo gamer ✨")










