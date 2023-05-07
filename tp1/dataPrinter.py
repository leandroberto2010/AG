from funciones import get_fitness
from funciones import funcion_objetivo

def mostrar_poblacion(poblacion, i):
    print(f"---------- GENERACIÓN {i} ----------")
    poblacion.sort(reverse=True, key=get_fitness)
    
    for ind in poblacion:
        print(f"[{poblacion.index(ind)}] x = {ind.x_value} \tf(x) = {funcion_objetivo(ind.x_value)} \tFitness = {ind.fitness:.2f} \tCromosoma: {ind.cromosoma} \tPrev x = {ind.get_prev_x()}")

def mostrar_padres(padres):
    print("##### PADRES SELECCIONADOS #####")
    
    for padre in padres:
        print(f"[{padres.index(padre)}] x = {padre.x_value} \tf(x) = {padre.y_value} \tFitness = {padre.fitness:.2f} \tCromosoma: {padre.cromosoma}")
        

