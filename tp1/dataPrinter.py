from tabulate import tabulate
from estadisticas import calc_promedio
import logging

reset = "\033[1;0m"
rojo = "\033[1;31m"
verde = "\033[1;32m"
amarillo = "\033[1;33m"

def mostrar_MMP(poblacion, i):
    print(f"{reset}-------------- GENERACIÓN [{i}] --------------")
    print(f"{verde}Maximo")
    print(f"x = {poblacion[0]['x']}\t f(x) = {poblacion[0]['y']}\t Cromosoma = {poblacion[0]['cromosoma']}")
    print(f"{rojo}Minimo")
    print(f"x = {poblacion[9]['x']}\t f(x) = {poblacion[9]['y']}\t Cromosoma = {poblacion[9]['cromosoma']}")
    print(f"{amarillo}Promedio = {calc_promedio(poblacion)}")
    logging.info(f"Maximo generacion {i}")
    logging.info(f"X = {poblacion[0]['x']}\t  f(x) = {poblacion[0]['y']}\t Cromosoma = {poblacion[0]['cromosoma']}\n")
    logging.info(f"Minimo")
    logging.info(f"X = {poblacion[9]['x']}\t  f(x) = {poblacion[9]['y']}\t Cromosoma = {poblacion[9]['cromosoma']}\n")
    logging.info(f"Promedio= {calc_promedio(poblacion)}\n")

def mostrar_poblacion(poblacion, i):
    poblacion.sort(reverse=True, key = lambda ind: ind["fitness"])
    print(f"\033[1;32m-------------- GENERACIÓN [{i}] --------------")
    print("\033[0;37m" + tabulate(poblacion, headers="keys", showindex="always", tablefmt="grid", floatfmt=".8f"))
    print()

def mostrar_padres(padres):
    print("\033[0;37m" + tabulate(padres, headers="keys", showindex="always", tablefmt="grid", floatfmt=".4f"))
    print()