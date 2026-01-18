'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.
Considerar que 'list_numbers' debe contener valores numéricos enteros mayores
o iguales a '0', en caso contrario se debe mostrar un error tipo 'ValueError'.

El error lo puedes mostrar con la siguiente instrucción:    
raise ValueError("MENSAJE DE ERROR")

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.
Considereu que 'list_numbers' ha de contenir valors numèrics enters majors
o iguals a '0', en cas contrari cal mostrar un error tipus 'ValueError'.

L'error el pots mostrar amb la següent instrucció:
raise ValueError("MISSATGE D'ERROR")

Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    # Validación 1: Verificar que sea una lista
    if not isinstance(list_numbers, list):
        raise ValueError("El parámetro debe ser una lista")
    
    # Validación 2: Verificar que la lista no esté vacía
    if len(list_numbers) == 0:
        raise ValueError("La lista no puede estar vacía")
    
    # Validación 3: Verificar que todos los elementos sean enteros positivos (>= 0)
    for num in list_numbers:
        if not isinstance(num, int):
            raise ValueError("Todos los elementos deben ser números enteros")
        if num < 0:
            raise ValueError("Todos los números deben ser mayores o iguales a 0")
    
    # Sumar solo los números impares
    suma = 0
    for num in list_numbers:
        if num % 2 != 0:  # Si el resto de dividir entre 2 es diferente de 0, es impar
            suma += num
    
    return suma


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
print(sum_odd_numbers([ 2, 4, 6, 8]))
print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
print(sum_odd_numbers([1, 3, 5, 9]))