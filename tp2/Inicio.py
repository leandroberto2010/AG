from greedy import greedy
from exhaustivo import exhaustivo
from exhaustivo import mejor_combinacion
from exhaustivo import load_items
from timeit import default_timer as timer
import pandas as pd


items = load_items('items.csv') #items/pesos .csv
capacidad = 4200 #4200/3000

#GREEDY
start = timer()
valor_total, items_seleccionados = greedy(items, capacidad)
end = timer()
greedy_time = end - start

print('--------- GREEDY --------- ')
print(pd.DataFrame(items_seleccionados))
print("Valor total de la mochila:", valor_total)
print('---------------------------------')

#BUSQUEDA EXHAUSTIVA CON RECURSIVIDAD
start = timer()
mejor_combinacion, mejor_valor = mejor_combinacion(items, capacidad)
end = timer()
rec_time = end - start
print('---------  RECURSIVIDAD --------- ')
print(pd.DataFrame(mejor_combinacion))
print(f"Valor total: {mejor_valor}")
print('------------------------------')

#BUSQUEDA EXHAUSTIVA
start = timer()
lista2 = exhaustivo(items, capacidad)
end = timer()
binary_time = end - start
print('---------  Exhaustiva normal --------- ')
print(pd.DataFrame(lista2[0]))
print('Valor total: ', pd.DataFrame(lista2[0])['valor'].sum())
print('---------------------------------')

print('--------- TIEMPO DE EJECUCIÓN ---------')
print("Greedy: \t\t", round(greedy_time * 1000, 3), 'ms')
print("Exhaustiva con rec.:\t", round(rec_time * 1000, 3), 'ms')
print("Exhaustiva sin rec.: \t", round(binary_time * 1000, 3), 'ms')