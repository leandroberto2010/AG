import matplotlib.pyplot as plt


#Calculo de promedio
def calc_promedio(poblacion):
    valortotal = 0
    for ind in poblacion:
        valortotal += ind["y"]
    promedio = valortotal/len(poblacion)
    return promedio

def guardar_valores(poblacion, maximos, minimos, promedios):
    #Máximos
    valormax = max(poblacion, key=lambda x: x["fitness"])
    maximos.append(valormax["y"])

    #Mínimos
    valormin = min(poblacion, key=lambda x: x["fitness"])
    minimos.append(valormin["y"])

    #Promedios
    promedios.append(calc_promedio(poblacion))

def grafica_conjunta(minimos, promedios, maximos):
    plt.plot(maximos, color = "green", label = "Maximos")
    plt.plot(promedios, color = "yellow", label = "Promedios")
    plt.plot(minimos, color = "red", label = "Minimos")
    
    plt.legend()
    plt.ylabel("f(x)", fontsize = "20")
    plt.xlabel("Ciclo", fontsize = "20")
    plt.show()