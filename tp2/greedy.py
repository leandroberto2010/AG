def greedy(items, capacidad):
    n = len(items)
    # Creamos una lista de índices y la ordenamos por la relación valor/peso de forma descendente
    indexes = sorted(range(n), key=lambda i: items[i]['valor'] / items[i]['volumen'], reverse=True)

    valor_total = 0
    peso_total = 0
    items_seleccionados = []

    for i in indexes:
        if peso_total + items[i]['volumen'] <= capacidad:
            valor_total += items[i]['valor']
            peso_total += items[i]['volumen']
            items_seleccionados.append(items[i])

    return valor_total, items_seleccionados
