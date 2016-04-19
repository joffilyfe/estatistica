# -*- coding: utf-8 -*-
import dataset
from scipy import std, var, mean


db = dataset.connect('mysql://root@localhost/luciana')
table = db['prodeaf']


def calculate(length=None):
    size = length
    times = []
    words = table.find(table.table.columns.time_translate >= 1000,
                       table.table.columns.time_translate <= 20000,
                       _limit=1000, word_size=size)

    for w in words:
        time = (w['time_translate']-1000)/1000
        times.append(time)

    # Imprimindo a variância e desvio padrão
    print("Tamanho: {}, Média: {}, Variância: {}, desvio padrão: {}".format(
        size, mean(times), var(times), std(times)))


for n in range(5, 15):
    calculate(n)