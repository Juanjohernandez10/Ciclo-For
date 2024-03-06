papa = 0
yuca = 0
zanahoria = 0
tipo = int(input('1/papa 2/yuca 3/zanahoria: '))
if tipo == 1:
    for i in range(3):
        litros = int(input('cuantos litros gastaste-> '))
        papa += litros
    print(' los litros gastados fueron ', papa)

if tipo == 2:
    for i in range(2):
        litros = int(input('cuantos litros gastaste-> '))
        yuca += litros
    print(' los litros gastados fueron ', yuca)
if tipo == 3:
    for i in range(2):
        litros = int(input('cuantos litros gastaste-> '))
        zanahoria += litros
    print('los litros gastados en zanahoria son', zanahoria)