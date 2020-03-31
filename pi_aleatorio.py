# coding: utf-8
__author__ = "Raphael Frajuca"

# Importando módulo decimal do Python
from decimal import Decimal
from decimal import getcontext

# Importando módulo de datas e tempo
from time import time

def randomint():
    
    # Pegar milissegundos atuais
    milisegundos = time()

    # Calcular o valor de Pi usando valores padronizados. (Circunferência / Raio)

    # Pegar ultimos números do valor de milissegundos atuais se baseando no relógio da maquina.
    mili = int(str(int(round(time() * 1000)))[-5:-1])
    
    # Calcular valor de Pi com o número de casas decimais de acordo com o valor retornado pelos milissegundos.
    getcontext().prec = mili
    pi = str(Decimal(3550000000000000000000000000000000000000000000000000000000) / Decimal(1130000000000000000000000000000000000000000000000000000000))

    # Pegar o ultimo decimal do Pi e retornar 
    return(int(pi[-1]))