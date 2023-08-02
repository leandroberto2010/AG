class Objeto:
    def __init__(self, volumen, valor):
        self.volumen = volumen
        self.valor = valor

def mejor_combinacion(objetos, volumen_maximo):
    def generar_combinaciones(actual_combinacion, i, volumen_actual, valor_actual):
        nonlocal mejor_valor, mejor_combinacion
        global volumen
        
        #guardo la mejor combinacion que tenga el valor maximo
        if volumen_actual <= volumen_maximo and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_combinacion = actual_combinacion[:]
            volumen = volumen_actual
        
        if i == len(objetos) or volumen_actual > volumen_maximo:
            return
        
        #genera combinaciones teniendo en cuenta el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion + [objetos[i]], i+1,
                              volumen_actual + objetos[i].volumen, valor_actual + objetos[i].valor)
        
        #genera combinaciones sin incluir el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion, i+1, volumen_actual, valor_actual)
        
        #el resultado de ambas llamadas recursivas de generar_combinaciones me dara todas las combinaciones posibles en mi lista de objetos

    mejor_valor = 0
    mejor_combinacion = []
    generar_combinaciones([], 0, 0, 0)
    
    return mejor_combinacion, mejor_valor, volumen

objetos = [
    Objeto(150, 20),
    Objeto(325, 40),
    Objeto(600, 50),
    Objeto(805, 36),
    Objeto(430, 25),
    Objeto(1200, 64),
    Objeto(770, 54),
    Objeto(60, 18),
    Objeto(930, 46),
    Objeto(353, 28),
]

maxvol = 4200
mejor_combinacion, mejor_valor, volumen = mejor_combinacion(objetos, maxvol)

print("Mejor combinación:")
for objeto in mejor_combinacion:
    print(f"Volumen: {objeto.volumen}, Valor: {objeto.valor}")

print(f"Mejor valor total: {mejor_valor}")
print(f"Volumen utilizado: {volumen}")