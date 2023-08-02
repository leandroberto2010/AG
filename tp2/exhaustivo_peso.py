class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

def mejor_combinacion(objetos, peso_maximo):
    def generar_combinaciones(actual_combinacion, i, peso_actual, valor_actual):
        nonlocal mejor_valor, mejor_combinacion
        global peso
        
        #guardo la mejor combinacion que tenga el valor maximo
        if peso_actual <= peso_maximo and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_combinacion = actual_combinacion[:]
            peso = peso_actual
        
        if i == len(objetos) or peso_actual > peso_maximo:
            return
        
        #genera combinaciones teniendo en cuenta el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion + [objetos[i]], i+1,
                              peso_actual + objetos[i].peso, valor_actual + objetos[i].valor)
        
        #genera combinaciones sin incluir el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion, i+1, peso_actual, valor_actual)
        
        #el resultado de ambas llamadas recursivas de generar_combinaciones me dara todas las combinaciones posibles en mi lista de objetos

    mejor_valor = 0
    mejor_combinacion = []
    generar_combinaciones([], 0, 0, 0)
    
    return mejor_combinacion, mejor_valor, peso

objetos = [
    Objeto(1800, 72),
    Objeto(600, 36),
    Objeto(1200, 60),
]

maxpeso = 3000
mejor_combinacion, mejor_valor, peso = mejor_combinacion(objetos, maxpeso)

print("Mejor combinación:")
for objeto in mejor_combinacion:
    print(f"Peso: {objeto.peso}, Valor: {objeto.valor}")

print(f"Mejor valor total: {mejor_valor}")
print(f"Peso utilizado: {peso}")