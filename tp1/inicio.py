import funciones as fc
import dataPrinter

poblacion = []
padres = []
cross_rate = 0.75
mut_rate = 0.05
cantidad = 10
ciclos = 20

fc.iniciar_poblacion(poblacion, cantidad, x_min=0, x_max=(2**30)-1)
fc.evaluar(poblacion)
dataPrinter.mostrar_poblacion(poblacion, 0)

for i in range(ciclos):
    fc.seleccion(poblacion, padres)
    dataPrinter.mostrar_padres(padres)
    fc.crossover(poblacion, padres, cross_rate, mut_rate)
    fc.evaluar(poblacion)
    dataPrinter.mostrar_poblacion(poblacion, i+1)
    print("Promedio = ", fc.calc_promedio(poblacion))