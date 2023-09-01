from surface import Surface
import stats
import random
population=[]
elite_population =[]
padres = []
cross_rate=0.3
mut_rate = 0.05
cont =0

def init(population_size = 10, height = 10, width = 10, turbines = 25):
    for _ in range(population_size):
        surface = Surface(height=height, width=width, turbines=turbines)
        population.append(surface)

def elite(population):
    for i in range(2):
        elite_population.append(population.pop(0))
        
def evaluar(population):
    total = 0
    for ind in population:
        ind.power = ind.get_total_power()
        total += ind.objective_function()
    for ind in population:    
        ind.fitness = ind.objective_function() / total
    population.sort(key = lambda ind: (ind.power), reverse=True)

def mutacion(ind):
    global cont
    if ind.turbine_count() >0:
        if mut_rate > random.random():
            ind.swap_cell()
        cont+=1
    return ind

def crossover():
    def obtener_cromosoma(padres, cross_point):
        return padres[0].surface[:cross_point] + padres[1].surface[cross_point:]
    
    def realizar_crossover():
        cross_point = random.randint(0, padres[0].height)
        child1 = Surface()
        child2 = Surface()

        child1.set_surface(obtener_cromosoma(padres, cross_point))
        child2.set_surface(obtener_cromosoma(padres[::-1], cross_point))
        return child1, child2
    
    if cross_rate >= random.random():
        child1, child2 = realizar_crossover()

        while child1.turbine_count() > 25:
            child1.toggle_cell()
        while child2.turbine_count() > 25:
            child2.toggle_cell()
        
        hijos=[]
        hijos.append(child1)
        hijos.append(child2)


        return hijos
    else:
        return padres

def torneo():
    contendientes = []
    while (len(padres)<2):
        for _ in range(4):
            posicion = random.randint(0, len(population)-1)
            contendientes.append(population[posicion])  
        padres.append(max(contendientes, key=lambda cont: cont.fitness))
        (max(contendientes, key=lambda cont: cont.fitness))   
        contendientes.clear()

ciclos=500
next_generation=[]
maximos = []
minimos = []
promedios = []
init(population_size=10, height=10, width=10, turbines=25)
evaluar(population)
stats.save_data(population, maximos, minimos, promedios)
for _ in range(ciclos):
    #elite(population)
    while len(next_generation)<len(population):
        padres.clear()
        torneo()
        next_generation.extend(crossover())
        population.clear()
        for pop in next_generation:
            population.append(mutacion(pop))
    next_generation.clear()
    #population.extend(elite_population)
    #elite_population.clear()
    evaluar(population)
    stats.save_data(population, maximos, minimos, promedios)
print(cont)

stats.grafica(maximos, minimos, promedios)