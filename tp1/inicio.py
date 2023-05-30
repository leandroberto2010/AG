import logging
import pandas as pd
from funciones import iniciar_poblacion
from funciones import evolucion
from estadisticas import guardar_valores
from estadisticas import grafica_conjunta

# Configuracion del logging
# Esto es para ver algunos resultados en un archivo (ver funcion mutacion)
# En la consola solo mostramos maximo, minimo y promedio como pide el enunciado
logging.basicConfig(filename='info.log', encoding='utf-8', level=logging.INFO, filemode="w") 

poblacion = []
maximos = []
minimos = []
promedios = []
ciclos = 100
uri = "C:/Users/leand/Documents/facultad/algoritmos/tpFinal/tpfinalfinal/data.xlsx" #Directorio donde se va a guardar el archivo excel

iniciar_poblacion(poblacion, 
                  cantidad = 10, 
                  x_min = 0, 
                  x_max = (2**30)-1)

guardar_valores(poblacion, maximos, minimos, promedios)

for i in range(ciclos):
    poblacion = evolucion(metodo = "ruleta", 
                          elitismo = False, 
                          cross_rate = 0.75, 
                          mut_rate = 0.30,
                          poblacion = poblacion)
    
    guardar_valores(poblacion, maximos, minimos, promedios)


valores = {
    "Maximos": maximos,
    "Minimos": minimos,
    "Promedios": promedios
}
df = pd.DataFrame(valores)
df.to_excel(uri, sheet_name="pag")

print(df)

grafica_conjunta(minimos, promedios, maximos)
