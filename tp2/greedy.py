class Objeto:
    def __init__(self, volumen, valor):
        self.volumen = volumen
        self.valor = valor


def greedy(objetos, volumen_maximo):
    volumen_actual = 0
    valor_actual = 0
    misobj=[]
    for i in range(len(objetos)-1):
        if ((volumen_actual+objetos[i].volumen) <= volumen_maximo):
                misobj.append(objetos[i])
                volumen_actual = volumen_actual + objetos[i].volumen
                valor_actual = valor_actual + objetos[i].valor
    return misobj, valor_actual, volumen_actual




objetos = [
    Objeto(150, 20),
    Objeto(325, 40),
    Objeto(600, 50),
    Objeto(805, 36),
    Objeto(430, 25),
    Objeto(1200, 64),
    Objeto(770, 54),
    Objeto(60, 18),
    Objeto(930, 46),
    Objeto(353, 28),
]

objetos.sort(key=lambda x: x.valor, reverse=True)
maxvol = 4200
misobj, valor, vol = greedy(objetos, maxvol)

print("Objetos: ")
for i in objetos:
    print(f"Volumen: {i.volumen}, Valor: {i.valor}")

print("Combinacion: ")
for objeto in misobj:
     print(f"Volumen: {objeto.volumen}, Valor: {objeto.valor}")

print(f"Valor: {valor}")
print(f"Volumen total: {vol}")