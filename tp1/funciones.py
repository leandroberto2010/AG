import random

class Individuo():
    x_value = 0
    y_value = 0
    cromosoma = ''
    crom_anterior = ''
    fitness = 0

    def set_x_value(self, x_value):
        self.x_value = x_value
        self.cromosoma = format(self.x_value, '010b')

    def set_cromosoma(self, cromosoma):
        self.cromosoma = cromosoma
        self.x_value = int(cromosoma, 2)

    def get_prev_x(self):
        if self.crom_anterior != "":
            return int(self.crom_anterior, 2)
        else:
            return ""

def iniciar_poblacion(poblacion, cantidad, x_min, x_max):
    for i in range(cantidad):
        ind = Individuo()
        ind.set_x_value(random.randint(x_min, x_max))
        poblacion.append(ind)

def funcion_objetivo(x):
    return x/(2**30-1)

def evaluar(poblacion):
    total = 0
    for ind in poblacion:
        total += funcion_objetivo(ind.x_value)
    for ind in poblacion:
        ind.fitness = funcion_objetivo(ind.x_value) / total

def seleccion(poblacion, padres):
    fitness = []
    padres.clear()
    for ind in poblacion:
        fitness.append(ind.fitness) 
    padres.extend(random.choices(poblacion, fitness, k=2)) #por que 4?

def mutacion(hijo, mut_rate): #esta en binario el cromosoma?
    nuevo = ''
    for gen in hijo.cromosoma:
        if mut_rate >= random.random():
            if gen == '1':
                nuevo += '0'
            else:
                nuevo += '1'
        else:
            nuevo += gen
    if nuevo != hijo.cromosoma:
        hijo.crom_anterior = hijo.cromosoma
        hijo.set_cromosoma(nuevo)

def crossover(poblacion, padres, cross_rate, mut_rate):
    cross_point = random.randint(1, 9)
    if cross_rate >= random.random():
        cromosoma = padres[1].cromosoma[:cross_point] + padres[0].cromosoma[cross_point:]
        hijo_1 = Individuo()
        hijo_1.set_cromosoma(cromosoma)
        mutacion(hijo_1, mut_rate)
        poblacion.append(hijo_1)
        print("Hijo 1 binario = ", hijo_1.cromosoma, " Valor= ", hijo_1.x_value)

        cromosoma = padres[0].cromosoma[:cross_point] + padres[1].cromosoma[cross_point:]
        hijo_2 = Individuo()
        hijo_2.set_cromosoma(cromosoma)
        mutacion(hijo_2, mut_rate)
        poblacion.append(hijo_2)
        print ("Hijo 2 binario=  ", hijo_2.cromosoma, " Valor= ", hijo_2.x_value)


def get_fitness(ind):
    return ind.fitness