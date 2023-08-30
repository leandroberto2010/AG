from surface import Surface
import stats
import random

forbidden_locations = []
CROSS_RATE = 0.75
MUT_RATE = 0.05
CYCLES = 200
population = []
padres = []
next_generation = []
maximos = []
minimos = []
promedios = []

def init(population_size = 10, height = 10, width = 10, turbines = 25):
    for _ in range(population_size):
        surface = Surface(height=height, width=width, turbines=turbines)
        population.append(surface)

def evaluar():
    total = 0
    for ind in population:
        total += ind.objective_function()
    for ind in population:    
        ind.fitness = ind.objective_function() / total
    population.sort(key = lambda ind: (ind.fitness), reverse=True)

def torneo():
    contendientes = []
    while (len(padres)<2):
        for _ in range(4):
            posicion = random.randint(0, len(population)-1)
            contendientes.append(population[posicion])  
        padres.append(max(contendientes, key=lambda cont: cont.fitness))
        (max(contendientes, key=lambda cont: cont.fitness))   
        contendientes.clear()

def ruleta():
    while (len(padres)<2):
        acum = 0   
        for ind in population:
            peso = random.uniform(0, 1)
            acum += ind.fitness
            if acum > peso:
                padres.append(ind)
                break

def seleccion(metodo):
    if (metodo == "ruleta"):
        return ruleta()
    if (metodo == "torneo"):
        return torneo()
    
def crossover():
    def obtener_cromosoma(padres):
        return padres[0].surface[:cross_point] + padres[1].surface[cross_point:]
    
    if CROSS_RATE >= random.random():
        cross_point = random.randint(0, padres[0].height)
        child1 = Surface()
        child2 = Surface()

        child1.set_surface(obtener_cromosoma(padres))
        child2.set_surface(obtener_cromosoma(padres[::-1]))

        if (child1.turbine_count()>25 or child2.turbine_count()>25):
            crossover()

        mutacion(child1)
        mutacion(child2)

        next_generation.append(child1)
        next_generation.append(child2)
    else:
        for padre in padres:
            mutacion(padre)
        next_generation.extend(padres)

def mutacion(ind):
    isFull = False
    if ind.turbine_count() >= 25: isFull = True
    if MUT_RATE > random.random():
        ind.toggle_cell(isFull)


init(population_size=30, height=10, width=10)
evaluar()
for _ in range(CYCLES):
    while (len(next_generation) < len(population)):
        padres.clear()
        seleccion('ruleta')
        crossover()
    population = next_generation.copy()
    evaluar()
    stats.save_data(population, maximos, minimos, promedios)
    next_generation.clear()

for ind in population:
    ind.print_surface()
    print('Turbinas:', ind.turbine_count())
    print('Potencia total: ', ind.get_total_power())
    print('Potencia media:', ind.get_average_power())
    print('Fitness:', ind.fitness)
    print('---------')

stats.grafica(maximos, minimos, promedios)