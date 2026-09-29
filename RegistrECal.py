def mostrar_encabezado_escuela():
    print("Instituto: Universidad Tecnologica de Xicotepec de Juarez Puebla UTXJ")
    print("REGISTRO Y EVALUACION DE CALIFICACIONES")

def obtener_nota_minima_aprobatoria():
    return 6.0

def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    else: 
        return "Excelente"

def calcular_promedio_ponderado(nota_examenes,nota_tareas):
    calificacion_final = (nota_examenes * 0.70) + (nota_tareas * .30)
    return calificacion_final

def generar_boleta(nombre_alumno,nota_examenes,nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = obtener_nota_minima_aprobatoria()
    estado_academico = evaluar_rendimiento(nota_final)
    print("------------------------------------------------------------------------------------")
    mostrar_encabezado_escuela()
    print("------------------------------------------------------------------------------------")
    print(f"Nombre: {nombre_alumno}")
    print(f"Calificacion minima aprobatoria:  {nota_minima}")
    print(f"Nota final: {nota_final}")
    print(f"Estado Academico: {estado_academico}")
    if nota_final < nota_minima:
        print("EL ALUMNO DEBE PRESENTAR EXAMEN EXTRAORDINARIO")
    else:
        print("EL ALMUNO PASO, FELICIDADES :D")

generar_boleta("Josue Leyva", 8.5, 9.0)
