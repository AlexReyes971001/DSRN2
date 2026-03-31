def contar_Caracteres(arg1="Aprender Python es divertido"):
    print(f"La frase {arg1} tiene {len(arg1)} caracteres")

contar_Caracteres("Esto es una prueba de función usando len")

print("")

def convertir_numero (numero):
    var1 = str(numero)
    var2 = float(numero)
    print(f"Entero: {numero}, Tipo: {type(numero)}")
    print(f"Cadena: {var1}, Tipo: {type(var1)}")
    print(f"Flotante: {var2}, Tipo: {type(var2)}")

convertir_numero(45)