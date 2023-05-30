import random


def funcion_objetivo(x):
    return (x/(2**30-1))**2

#El individuo se puede crear a partir de un valor random de x al iniciar la poblacion
#Individuo es un diccionario
def crear_individuo(cromosoma = None, x = None):
    individuo = {}
    if (cromosoma != None): #Se genera el valor X mediante su cromosoma que esta en binario en caso de que haya habido mutacion
        individuo = {
            "x": int(cromosoma, 2),
            "y": funcion_objetivo(int(cromosoma, 2)),
            "cromosoma": cromosoma,
            "fitness": 0 
        }
    else:
        individuo = { #se asigna valor X y este genera el cromosoma en binario
            "x": x,
            "y": funcion_objetivo(x),
            "cromosoma": format(x, "030b"),
            "fitness": 0 
        }
    return individuo

#Se genera una poblacion aleatoria
def iniciar_poblacion(poblacion, cantidad, x_min, x_max):
    for _ in range(cantidad):
        individuo = crear_individuo(x = random.randint(x_min, x_max))
        poblacion.append(individuo)
    evaluar(poblacion)
    poblacion.sort(reverse=True, key = lambda ind: ind["fitness"])

#Calculo de fitness total y de cada individuo
def evaluar(poblacion):
    total = 0
    for ind in poblacion:
        total += ind["y"]
    for ind in poblacion:
        ind["fitness"] = ind["y"]/total

#Seleccion mediante torneo
def torneo(poblacion):
    padres = []
    contendientes = []
    while (len(padres)<2):
        for i in range(4):
            posicion = random.randint(0, len(poblacion)-1) #genero 4 posiciones aleatorias
            contendientes.append(poblacion[posicion])  
        padres.append(max(contendientes, key=lambda cont: cont["fitness"])) #el que tenga un mayor fitness de los contendientes sera un padre
        contendientes.clear()
    return padres

#Seleccion mediante ruleta
def ruleta(poblacion):
    padres = []
    while (len(padres)<2):
        acum = 0        #seleccion por ruleta mediante acumulacion de fitness
        for ind in poblacion:
            peso = random.uniform(0, 1)
            acum += ind["fitness"]
            if acum >= peso:
                padres.append(ind)
                break
    return padres

#Seleccion de metodo
def seleccion(poblacion, metodo):
    if (metodo == "ruleta"):
        return ruleta(poblacion)
    if (metodo == "torneo"):
        return torneo(poblacion)


def mutacion(hijo, mut_rate):
    if (mut_rate >= random.random()):
        posicion = random.randint(0, len(hijo["cromosoma"])-1) #genero posicion aleatoria
        cromosoma = list(hijo["cromosoma"])
        if cromosoma[posicion] == '0':
            cromosoma[posicion] = '1'
        else:
            cromosoma[posicion] = '0'
        hijo["x"] = int("".join(cromosoma), 2)
        hijo["y"] = funcion_objetivo(int("".join(cromosoma), 2))
        hijo["cromosoma"] = "".join(cromosoma)



#Se realiza el crossover
def crossover(padres, cross_rate):
    #Realiza el corte en el cromosoma de los padres y lo devuelve
    def obtener_cromosoma(padres):
        return padres[0]["cromosoma"][:cross_point] + padres[1]["cromosoma"][cross_point:]
    
    hijos = []
    if cross_rate >= random.random():
        cross_point = random.randint(0, len(padres[0]["cromosoma"]))

        crom = obtener_cromosoma(padres)
        hijos.append(crear_individuo(cromosoma = crom))

        crom = obtener_cromosoma(padres[::-1]) #Le pasamos los padres en orden invertido
        hijos.append(crear_individuo(cromosoma = crom))
    else:
        hijos = padres #Si no hubo crossover los padres pasan a ser hijos
    return hijos

#Se realiza la evolucion de la poblacion
def evolucion(poblacion, metodo, elitismo, cross_rate, mut_rate):
    nueva_gen = []

    if (elitismo):
        for i in range(2):
            maximo = max(poblacion, key=lambda x: x["fitness"]) #Se seleccionan a los dos mejores valores de la poblacion
            nueva_gen.append(maximo)
            poblacion.remove(maximo)

    for i in range(int(len(poblacion)/2)):
        padres = seleccion(poblacion, metodo) #La seleccion devuelve 2 candidatos
        hijos = crossover(padres, cross_rate) #Devuelve dos hijos
        for hijo in hijos:
            mutacion(hijo, mut_rate)
        nueva_gen.extend(hijos)
        evaluar(nueva_gen)
    nueva_gen.sort(reverse=True, key = lambda ind: ind["fitness"])
    return nueva_gen
