import datetime as dt

"""
6 - Uma partida de futebol iniciou na hora A e terminou na hora B. Faça um algoritmo que
calcule o tempo que durou a partida.
"""

hstart = int(input('Digite a hora de início da partida: '))
mmstart = int(input('Digite os minutos de início da partida: '))
hend = int(input('Digite a hora que a partira encerrou: '))
mmend = int(input('Digite os minutos em que a partira encerrou: '))

start = "{}:{}".format(hstart, mmstart)
end = "{}:{}".format(hend, mmend)
start_dt = dt.datetime.strptime(start, '%H:%M')
end_dt = dt.datetime.strptime(end, '%H:%M')
diff = (end_dt - start_dt)
print('A partida durou: {} horas'.format(diff))
