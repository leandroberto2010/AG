import csv

def load_items(file):
    items = []
    with open(file, 'r') as items_file:
        reader = csv.DictReader(items_file)
        for record in reader:
            record['volumen'] = int(record['volumen'])
            record['valor'] = int(record['valor'])
            items.append(record)
    return items

def powerset(list):
    n = len(list)
    x = 2**n
    for i in range(1, x):
        binary = bin(i)[2:].zfill(n)
        subset = []
        for j in range(n):
            if binary[j] == '1':
                subset.append(list[j])
        yield subset

def weight_and_value(set):
    volumen_total = 0
    valor_total = 0
    for item in set:
        volumen_total += item['volumen']
        valor_total += item['valor']         
    return volumen_total, valor_total

def exhaustivo(items, capacity): 
    lista = []
    max_value = 0
    for set in powerset(items):
        volumen_total, valor_total = weight_and_value(set) 
        if volumen_total <= capacity:
            if valor_total > max_value:
                max_value = valor_total
                lista.clear()
                lista.append(set)
            elif valor_total == max_value:
                lista.append(set)
    return lista

def mejor_combinacion(objetos, volumen_maximo):
    def generar_combinaciones(actual_combinacion, i, volumen_actual, valor_actual):
        nonlocal mejor_valor, mejor_combinacion
        
        #guardo la mejor combinacion que tenga el valor maximo
        if volumen_actual <= volumen_maximo and valor_actual > mejor_valor:
            mejor_valor = valor_actual
            mejor_combinacion = actual_combinacion[:]
        
        if i == len(objetos) or volumen_actual > volumen_maximo:
            return
        
        #genera combinaciones teniendo en cuenta el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion + [objetos[i]], 
                                                            i+1,
                                                            volumen_actual + objetos[i]['volumen'], 
                                                            valor_actual + objetos[i]['valor'])
        
        #genera combinaciones sin incluir el objeto en el que me encuentro en este momento
        generar_combinaciones(actual_combinacion, i+1, volumen_actual, valor_actual)
        
        #el resultado de ambas llamadas recursivas de generar_combinaciones me dara todas las combinaciones posibles en mi lista de objetos
    mejor_valor = 0
    mejor_combinacion = []
    generar_combinaciones([], 0, 0, 0)
    
    return mejor_combinacion, mejor_valor