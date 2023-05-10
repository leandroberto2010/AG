import funciones as fc
import dataPrinter

poblacion = []
poblacion_elitismo = []
padres = []
mejores = []
maximos = []
minimos = []
promedios = []

cross_rate = 0.75
mut_rate = 0.05
cantidad = 10
ciclos = 100
elitismo = False

fc.iniciar_poblacion(poblacion, cantidad, x_min=0, x_max=(2**30)-1)
fc.evaluar(poblacion)
dataPrinter.mostrar_poblacion(poblacion, 0)
print(f"############PROMEDIO GENERACION {0} ############ ")
print("Promedio = ", fc.calc_promedio(poblacion))
fc.guardar_valores(poblacion, maximos, minimos, promedios)

for i in range(ciclos):
    if elitismo:
        fc.salvar_mejores(mejores, poblacion)
    fc.seleccion(poblacion, padres)
    dataPrinter.mostrar_padres(padres)
    fc.crossover(poblacion, padres, cross_rate, mut_rate)
    if elitismo:
        fc.insertar_mejores(mejores, poblacion)
    fc.evaluar(poblacion)
    dataPrinter.mostrar_poblacion(poblacion, i+1)
    print(f"############PROMEDIO GENERACION {i+1} ############ ")
    print("Promedio = ", fc.calc_promedio(poblacion))
    fc.guardar_valores(poblacion, maximos, minimos, promedios)

fc.grafica_maximo(maximos)
fc.grafica_minimo(minimos)
fc.grafica_promedio(promedios)