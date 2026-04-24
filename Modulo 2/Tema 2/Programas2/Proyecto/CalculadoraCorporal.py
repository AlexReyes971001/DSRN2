def calcular_imc(peso_kg, altura_m):
    """
    Calcula el Índice de Masa Corporal (IMC).
	Fórmula: IMC = peso / (altura^2)	 
	Parámetros:
	peso_kg (float): Peso en kilogramos
	altura_m (float): Altura en metros	 
	Retorna:
	float: El IMC calculado
    """
    return peso_kg / (altura_m ** 2)

def es_peso_saludable(imc):
    """Determina si el IMC está e rango saludable (18.5 - 24.9)
    Parámetro:
    imc (float): Índice de Masa Corporal
    Retorna:
    bool: True si está en rango saludable, False si no
    """
    return imc >= 18.5 and imc <= 24.9

def tiene_sobrepeso(imc):
    """
    Determina si hay sobrepeso (IMC >= 25).
    """
    return imc >= 25

def tiene_bajo_peso(imc):
    """
    Determina si hay bajo peso (IMC < 18.5).
    """
    return imc < 18.5

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.
    Parámetros:
    peso_kg (float): Peso en kg
    altura_cm (float): Altura en cm
    edad (int): Edad en años
    es_hombre (bool): True si es hombre, False si es mujer 
    Retorna:
    float: Calorías diarias recomendadas
    """
    if es_Hombre == True:
        calorias = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    if es_Hombre == False:
        calorias = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)
    # es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer
    return calorias

def calcular_agua_diaria(peso_kg):
    """
    Calcula litros de agua recomendados al día (35ml por kg de peso).
    """
    return (peso_kg * 35) / 1000

def calcular_ritmo_cardiaco_maximo(edad):
    """
    Calcula el ritmo cardíaco máximo (220 - edad).
    """
    return 220 - edad
	

edad = 29
peso = 67.8
estatura_m = 1.7
es_Hombre = True
estatura_cm = estatura_m * 100
imc = calcular_imc(peso,estatura_m)

print(f"Tu IMC es: {imc}")
print(f"¿Tu peso es saludable?: {es_peso_saludable(imc)}")
print(f"¿Actualmente cuentas con sobrepeso?: {tiene_sobrepeso(imc)}")
print(f"¿Actualmente tu peso es muy bajo?: {tiene_bajo_peso(imc)}")
print(f"Tus calorias diarias son: {calcular_calorias_diarias(peso,estatura_cm,edad,es_Hombre)}")
print(f"Se recomienda que tomes {calcular_agua_diaria(peso)} litros de agua al dia")
print(f"Tu ritmo cardíaco maximo es de: {calcular_ritmo_cardiaco_maximo(edad)}")