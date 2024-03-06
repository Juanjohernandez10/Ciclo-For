etapas = int(input('etapas recorridas -> '))
km_recorridos = 0

for i in range(etapas):
    distancia = int(input('distancia-> '))
    km_recorridos += distancia
print('distancia recorrida ', km_recorridos)
print('por etapas', etapas)
