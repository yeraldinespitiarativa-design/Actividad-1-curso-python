def ingresar_calificaciones():
    """
    Permite al usuario introducir nombres de materias y sus calificaciones.
    Retorna dos listas: una con los nombres de las materias y otra con las calificaciones.
    """
    materias = []
    calificaciones = []
    
    print("--- Ingreso de Materias y Calificaciones ---")
    while True:
        materia = input("Ingresa el nombre de la materia: ").strip()
        if not materia:
            print("El nombre de la materia no puede estar vacío. Inténtalo de nuevo.")
            continue
            
        while True:
            try:
                calificacion = float(input(f"Ingresa la calificación para '{materia}' (entre 0 y 10): "))
                if 0 <= calificacion <= 10:
                    break
                else:
                    print("Error: La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Error: Por favor ingresa un número válido.")
                
        materias.append(materia)
        calificaciones.append(calificacion)
        
        continuar = input("¿Deseas ingresar otra materia? (s/n): ").strip().lower()
        if continuar != 's':
            break
            
    return materias, calificaciones

def calcular_promedio(calificaciones):
    """
    Recibe una lista de calificaciones y devuelve el promedio de todas ellas.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)

def determinar_estado(calificaciones, umbral=5.0):
    """
    Recibe la lista de calificaciones y un valor umbral.
    Devuelve dos listas: índices de materias aprobadas y de materias reprobadas.
    """
    aprobadas = []
    reprobadas = []
    
    for i, calificacion in enumerate(calificaciones):
        if calificacion >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)
            
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones):
    """
    Identifica el índice de la calificación más alta y el índice de la más baja.
    """
    if not calificaciones:
        return -1, -1
        
    idx_max = calificaciones.index(max(calificaciones))
    idx_min = calificaciones.index(min(calificaciones))
    
    return idx_max, idx_min

def main():
    print("Bienvenido a la Calculadora de Promedios Escolares\n")
    
    # 1. Obtener datos del usuario
    materias, calificaciones = ingresar_calificaciones()
    
    if not materias:
        print("\nNo se ingresaron materias. Saliendo del programa.")
        print("¡Hasta luego!")
        return
        
    # 2. Calcular promedio
    promedio = calcular_promedio(calificaciones)
    
    # 3. Determinar materias aprobadas y reprobadas
    idx_aprobadas, idx_reprobadas = determinar_estado(calificaciones)
    
    # 4. Encontrar materias con calificaciones extremas
    idx_mejor, idx_peor = encontrar_extremos(calificaciones)
    
    # 5. Mostrar resumen final
    print("\n" + "="*40)
    print("RESUMEN FINAL")
    print("="*40)
    
    print("\n--- Todas las materias y calificaciones ---")
    for i in range(len(materias)):
        print(f"- {materias[i]}: {calificaciones[i]}")
        
    print(f"\n--- Promedio General ---")
    print(f"Promedio: {promedio:.2f}")
    
    print("\n--- Materias Aprobadas ---")
    if idx_aprobadas:
        for i in idx_aprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")
        
    print("\n--- Materias Reprobadas ---")
    if idx_reprobadas:
        for i in idx_reprobadas:
            print(f"- {materias[i]} ({calificaciones[i]})")
    else:
        print("Ninguna")
        
    print("\n--- Rendimiento Extremo ---")
    print(f"Mejor materia: {materias[idx_mejor]} con {calificaciones[idx_mejor]}")
    print(f"Peor materia: {materias[idx_peor]} con {calificaciones[idx_peor]}")
    
    print("\n" + "="*40)
    print("¡Gracias por utilizar la Calculadora de Promedios! Hasta luego.")

if __name__ == "__main__":
    main()
