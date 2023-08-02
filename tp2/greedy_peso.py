class Objeto:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor
        self.proporcion = valor/peso


def greedy(objetos, peso_maximo):
    peso_actual = 0
    valor_actual = 0
    misobj=[]
    for i in range(len(objetos)-1):
        if ((peso_actual+objetos[i].peso) <= peso_maximo):
                misobj.append(objetos[i])
                peso_actual = peso_actual + objetos[i].peso
                valor_actual = valor_actual + objetos[i].valor
    return misobj, valor_actual, peso_actual




objetos = [
    Objeto(1800, 72),
    Objeto(600, 36),
    Objeto(1200, 60),
]

objetos.sort(key=lambda x: x.proporcion, reverse=True)
maxvol = 4200
misobj, valor, vol = greedy(objetos, maxvol)

print("Objetos: ")
for i in objetos:
    print(f"Peso: {i.peso}, Valor: {i.valor}")

print("Combinacion: ")
for objeto in misobj:
     print(f"peso: {objeto.peso}, Valor: {objeto.valor}")

print(f"Valor: {valor}")
print(f"Peso total: {vol}")