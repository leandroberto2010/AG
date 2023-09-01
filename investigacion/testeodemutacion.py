from surface import Surface
import random

population = []
mut_rate = 0.05

def begin(population_size = 10, height = 10, width = 10, turbines = 25):
    for _ in range(population_size):
        surface = Surface(height=height, width=width, turbines=turbines)
        population.append(surface)

def mutacion(ind):
    isFull = False
    if ind.turbine_count() >= 25: isFull = True
    ind.toggle_cell(isFull)

begin(population_size=50, height=10, width=10, turbines=25)
for i in population:
    print("ORIGINAL: ")
    print(i.turbine_count())
    i.print_surface()
    if mut_rate > random.random():
        print("MUTADO:")
        mutacion(i)
        print(i.turbine_count())
        i.print_surface()
