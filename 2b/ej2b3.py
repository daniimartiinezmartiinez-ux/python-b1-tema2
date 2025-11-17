"""
Enunciado:
Implementa una función 'triangle_area_calculate', que recibe dos parámetros,
que corresponden a la altura y la base de un triángulo que deben
ser números positivos. Dichos parámetros deben ser nombrados correctamente,
considerando las buenas prácticas de programación PEP8.
La función debe retornar el cálculo del área de un triángulo mediante los
datos introducidos, adicionalmente, el código debe tener comentarios de manera
que se vaya explicando el procedimiento.

Parámetros:
Son dos parámetros, que corresponden a la altura y la base de
un triángulo y deben ser números positivos. Se deben crear correctamente
utilizando las buenas prácticas de programación PEP8.


Ejemplo:
    Entrada:
    triangle_area_calculate(33, 45)

    Salida:
    742.5


Enunciat:
Implementa una funció 'triangle_area_calculate', que rebi dos paràmetres,
que corresponen a l'alçada i la base d'un triangle i que han de
ser números positius. Aquests paràmetres han de ser nomenats correctament,
considerant les bones pràctiques de programació PEP8.
La funció ha de retornar el càlcul de l'àrea d'un triangle mitjançant les
dades introduïdes, addicionalment, el codi ha de tenir comentaris de manera
que es vagi explicant el procediment.

Paràmetres:
Són dos paràmetres, que corresponen a l'alçada i la base de
un triangle i que han de ser números positius. S'han de crear correctament
utilitzant les bones pràctiques de programació PEP8.


Exemple:
     Entrada:
     triangle_area_calculate(33, 45)

     Sortida:
     742.5

"""


def triangle_area_calculate(base, altura):
    
    #Comprobamos que los valores sean positivos
    if base < 0 or altura < 0:
        raise ValueError("La base y la altura deben ser positivos.")

    #Comprobamos que los valores sean enteros
    if not isinstance(base, int) or not isinstance(altura, int): #Comprobamos que el valor sea un entero, sino enviara ValueError
        raise ValueError("Los valores deben ser un número entero.")

    #Realizamos el calculo del area
    area = (base * altura) / 2
    return area

#Añadimos Try Except para capturar errores
try:
    base = 33
    altura = 45
    resultado = triangle_area_calculate(base, altura)
    print(f"Resultado final: {resultado}") #Si el programa se ejecuta de manera correcta imprimira el resultado
except ValueError as e:
    print(f"Error: {e}") #Si el programa detecta un error imprimira el problema detectado
    
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta
# el script

# Si vols provar el teu codi, descomenta les línies següents i executa
# l'scrip
