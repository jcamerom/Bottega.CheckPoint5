# Ejercicio 1: Cree un bucle For de Python
for num in range (1,10): # Empieza en el 1 y acaba en el 9
    print('Este es el número', num)
print("Bucle for finalizado")

# Ejercicio 2: Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
def suma(num1, num2, num3):
    print(f"Vamos a sumar tres números: {num1} + {num2} + {num3}")
    return print("El resultado es" , num1 + num2 + num3)

suma(4, 4.5, -2)

# Ejercicio 3: Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear.
sum_lam = lambda l_num1, l_num2, l_num3: l_num1 + l_num2 + l_num3

print("El resultado de sumar con la función lambda es", sum_lam(2.3, 5, -2))

# Ejercicio 4: Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no 
# con un valor de la lista. *Sugerencia, si es necesario, utilice un bucle for in y el operador in.
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
for name in lista_nombre:
    if nombre == name:
        print(f"Efectivamente, el nombre '{nombre}', sí está en la lista")
        break
else:
    print(f"El nombre '{nombre}' no está en la lista")
print("Programa finalizado")

