mi_arreglo = [10, 20, 30, 40, 50]

print(f"Arreglo inicial: {mi_arreglo}")

primer_elemento = mi_arreglo[0]
print(f"\n1. Acceso al índice 0: {primer_elemento} -> Complejidad: O(1)")


mi_arreglo.append(60)
print(f"2. Inserción al final (60): {mi_arreglo} -> Complejidad: O(1) amortizado")


mi_arreglo.insert(2, 25)
print(f"3. Inserción de 25 en índice 2: {mi_arreglo} -> Complejidad: O(n)")

elemento_buscar = 40
existe = elemento_buscar in mi_arreglo
print(f"4. Búsqueda del valor {elemento_buscar}: Encontrado={existe} -> Complejidad: O(n)")


mi_arreglo.remove(30)
print(f"5. Eliminación del valor 30: {mi_arreglo} -> Complejidad: O(n)")

ultimo = mi_arreglo.pop()
print(f"6. Eliminación del último elemento ({ultimo}): {mi_arreglo} -> Complejidad: O(1)")
