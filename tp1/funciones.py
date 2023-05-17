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

def mostrar_mejor(poblacion):
    valor_maximo = max(poblacion, key=lambda x: x.y_value)
    print('---------------------')
    print('VALOR MAXIMO: ', valor_maximo.x_value)
    print('VALOR MAXIMO DE FUNCION: ', valor_maximo.y_value)
    print('CROMOSOMA VALOR MAXIMO: ', valor_maximo.cromosoma)
    print('---------------------')
    
def torneo(poblacion, padres):
    contendientes = []
    padres.clear()
    while (len(padres)<2):
        for i in range(1, 4):
            posicion = random.randint(0, len(poblacion)-1) #genero 4 posiciones aleatorias
            contendientes.append(poblacion[posicion])  
        padres.append(max(contendientes, key=lambda x: x.fitness)) #el que tenga un mayor fitness de los contendientes sera un padre
    return padres

def ruleta(poblacion, padres):
    padres.clear()
    while (len(padres)<2):
        acum = 0        #seleccion por ruleta mediante acumulacion de fitness
        for i in poblacion:
            peso = random.uniform(0, 1)
            acum += i.fitness
            if acum > peso:
                padres.append(i)
                break
    return padres
        

#def seleccion(poblacion, padres): OBSOLETO
 #   fitness = []
  #  padres.clear()
   # for ind in poblacion:
    #    fitness.append(ind.fitness) 
    #padres.extend(random.choices(poblacion, fitness, k=2)) #desarrollar, no usar este metodo
    #while padres[0] == padres[1]: #evitar que tengan el mismo padre
    #  padres.pop(1)
     #   padres.extend(random.choices(poblacion, fitness, k=1))
    

def mutacion(hijo, mut_rate):
    if (mut_rate >= random.random()):
        posicion = random.randint(0, len(hijo.cromosoma)-1) #genero posicion aleatoria
        hijo.prev_x = hijo.cromosoma
        hijo_mutado = list(hijo.cromosoma)
        if hijo_mutado[posicion] == '0':
            hijo_mutado[posicion] = '1'
        else:
            hijo_mutado[posicion] = '0'
        hijo.set_cromosoma(''.join(hijo_mutado))
        print("------------------HUBO MUTACION------------------")
        print('VALOR MUTADO: ', hijo.x_value)
        print('CROMOSOMA MUTADO: ', hijo.cromosoma)
        return hijo
        
            

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
        mutacion(padres[0], mut_rate)
        mutacion(padres[1], mut_rate)
        nueva_gen.append(padres[0])
        nueva_gen.append(padres[1])
    return nueva_gen

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