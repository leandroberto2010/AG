import random
import matplotlib.pyplot as plt


class Individuo():
    x_value = 0
    y_value = 0
    cromosoma = ''
    crom_anterior = ''
    fitness = 0

    def set_x_value(self, x_value):
        self.x_value = x_value
        self.cromosoma = format(self.x_value, '010b')
    
    def set_y_value(self, y_value):
        self.y_value = y_value

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
    return (x/(2**30-1))**2

def evaluar(poblacion):
    total = 0
    for ind in poblacion:
        ind.set_y_value(funcion_objetivo(ind.x_value))
        total += funcion_objetivo(ind.x_value)
    for ind in poblacion:
        ind.fitness = funcion_objetivo(ind.x_value) / total

def seleccion(poblacion, padres):
    fitness = []
    padres.clear()
    for ind in poblacion:
        fitness.append(ind.fitness) 
    padres.extend(random.choices(poblacion, fitness, k=2))
    while padres[0] == padres[1]: #evitar que tengan el mismo padre
        padres.pop(1)
        padres.extend(random.choices(poblacion, fitness, k=1))
    

def mutacion(hijo, mut_rate):
    if (mut_rate < random.random()):
        indice1 = random.randint(0, len(hijo.cromosoma)-1)
        indice2 = random.randint(0, len(hijo.cromosoma)-1)
        start = max(indice1, indice2)
        end = min(indice1, indice2)
        for i in range(start, end):
            hijo.cromosoma[i] = 1 - hijo.cromosoma[i]
            

def crossover(nueva_gen, padres, cross_rate, mut_rate):
    cross_point = random.randint(0, len(padres[0].cromosoma))
    if cross_rate >= random.random():
        cromosoma = padres[1].cromosoma[:cross_point] + padres[0].cromosoma[cross_point:]
        hijo_1 = Individuo()
        hijo_1.set_cromosoma(cromosoma)
        print("Hijo 1 cromosoma = ", hijo_1.cromosoma, " Valor= ", hijo_1.x_value)
        mutacion(hijo_1, mut_rate)
        nueva_gen.append(hijo_1)

        cromosoma = padres[0].cromosoma[:cross_point] + padres[1].cromosoma[cross_point:]
        hijo_2 = Individuo()
        hijo_2.set_cromosoma(cromosoma)
        print("Hijo 2 cromosoma = ", hijo_2.cromosoma, " Valor= ", hijo_2.x_value)
        mutacion(hijo_2, mut_rate)
        nueva_gen.append(hijo_2)
    else:
        nueva_gen.append(padres[0])
        nueva_gen.append(padres[1])
    return nueva_gen
        ##poblacion.remove(padres[1]) #elimino a los padres de la poblacion
        ##poblacion.remove(padres[0])

def get_fitness(ind):
    return ind.fitness

def calc_promedio(poblacion):
    valortotal = 0
    for ind in poblacion:
        valortotal += ind.y_value
    promedio = valortotal/len(poblacion)
    return promedio

def salvar_mejores(mejores, poblacion): #guardo los mejores valores de acuerdo al fitness y los elimino de la poblacion para evitar que sean seleccionados en el crossover
    mejores.clear()
    max1 = max(poblacion, key=lambda x: x.fitness)
    mejores.append(max1)
    poblacion.remove(max1)
    max2= max(poblacion, key=lambda x: x.fitness)
    mejores.append(max2)
    poblacion.remove(max2)

def insertar_mejores(mejores, poblacion): #inserto de nuevo los mejores valores
    poblacion.extend(mejores)

def guardar_valores(poblacion, maximos, minimos, promedios):
    valormax = max(poblacion, key=lambda x: x.fitness)
    maximos.append(valormax.y_value)
    valormin = min(poblacion, key=lambda x: x.fitness)
    minimos.append(valormin.y_value)
    promedios.append(calc_promedio(poblacion))

def grafica_maximo(maximos):
    y = maximos
    plt.plot(y, marker = '.')
    plt.title("Maximos")
    plt.ylabel("Valor maximo")
    plt.xlabel("Ciclo")
    plt.show()

def grafica_minimo(minimos):
    y = minimos
    plt.plot(y, marker = '.')
    plt.title("Minimos")
    plt.ylabel("Valor minimo")
    plt.xlabel("Ciclo")
    plt.show()

def grafica_promedio(promedio):
    y = promedio
    plt.plot(y, marker = '.')
    plt.title("Promedios")
    plt.ylabel("Valor promedio")
    plt.xlabel("Ciclo")
    plt.show()

def grafica_conjunta(minimos, promedios, maximos):
    plt.plot(maximos, color = "green", label = "Maximos")
    plt.plot(promedios, color = "yellow", label = "Promedios")
    plt.plot(minimos, color = "red", label = "Minimos")
    
    plt.legend()
    plt.ylabel("f(x)", fontsize = "20")
    plt.xlabel("Ciclo", fontsize = "20")
    plt.show()