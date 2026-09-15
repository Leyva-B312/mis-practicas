"""
Ejemplo de Manipulación de Arreglos (Listas) en Python
Este script demuestra operaciones comunes sobre arreglos y documenta
su complejidad computacional usando Notación Big O.
"""

# Lista de ejemplo inicial (Arreglo dinámico)
mi_arreglo = [10, 20, 30, 40, 50]

print(f"Arreglo inicial: {mi_arreglo}")

# 1. Acceso por Índice -> O(1)
# El acceso a un elemento por su índice es constante porque la dirección de memoria se calcula directamente.
primer_elemento = mi_arreglo[0]
print(f"\n1. Acceso al índice 0: {primer_elemento} -> Complejidad: O(1)")

# 2. Inserción al final (Append) -> O(1) amortizado
# Agregar un elemento al final es constante la mayor parte del tiempo, salvo cuando el arreglo necesita redimensionar su memoria.
mi_arreglo.append(60)
print(f"2. Inserción al final (60): {mi_arreglo} -> Complejidad: O(1) amortizado")

# 3. Inserción en un índice específico -> O(n)
# Requiere desplazar todos los elementos posteriores a la derecha para hacer espacio.
mi_arreglo.insert(2, 25)
print(f"3. Inserción de 25 en índice 2: {mi_arreglo} -> Complejidad: O(n)")

# 4. Búsqueda por valor -> O(n)
# En el peor de los casos, recorre todo el arreglo para encontrar el elemento (Búsqueda Lineal).
elemento_buscar = 40
existe = elemento_buscar in mi_arreglo
print(f"4. Búsqueda del valor {elemento_buscar}: Encontrado={existe} -> Complejidad: O(n)")

# 5. Eliminación de un elemento por valor -> O(n)
# Requiere buscar el elemento y luego desplazar los demás a la izquierda para cubrir el hueco.
mi_arreglo.remove(30)
print(f"5. Eliminación del valor 30: {mi_arreglo} -> Complejidad: O(n)")

# 6. Eliminación del último elemento (Pop) -> O(1)
# Eliminar al final no requiere desplazar otros elementos.
ultimo = mi_arreglo.pop()
print(f"6. Eliminación del último elemento ({ultimo}): {mi_arreglo} -> Complejidad: O(1)")