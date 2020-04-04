# coding: utf-8
__author__ = "Raphael Frajuca"

# Importando módulo decimal do Python
from decimal import Decimal
from decimal import getcontext

# Importando módulo de  tempo
import time

def randomint(numero1, numero2 = None):
    
    tempo = int(str(time.perf_counter()).split('.')[1])
    
    if(numero1 != None and numero2 == None):
        getcontext().prec = tempo
        pi = str(Decimal(3550000000000000000000000000000000000000000000000000000000) / Decimal(1130000000000000000000000000000000000000000000000000000000))
        limite = (numero1-1)
        
        limite_caracteres = int("-"+str(len(str(limite))))-1
        
        pi_aleatorio = int(pi[limite_caracteres:-1])
        while(pi_aleatorio >= numero1):
            tempo = int(str(time.perf_counter()).split('.')[1]) 
            getcontext().prec = tempo
            pi = str(Decimal(3550000000000000000000000000000000000000000000000000000000) / Decimal(1130000000000000000000000000000000000000000000000000000000))
            limite = (numero1-1)
        
            limite_caracteres = int("-"+str(len(str(limite))))-1
        
            pi_aleatorio = int(pi[limite_caracteres:-1])
        return(pi_aleatorio)

    if(numero1 != None and numero2 != None and numero2 >= numero1):
        getcontext().prec = tempo
        pi = str(Decimal(3550000000000000000000000000000000000000000000000000000000) / Decimal(1130000000000000000000000000000000000000000000000000000000))
        limite = (numero2-1)

        limite_caracteres = int("-"+str(len(str(limite))))-1
        
        pi_aleatorio = int(pi[limite_caracteres:-1])
        while(pi_aleatorio not in range(numero1, numero2)):
            tempo = int(str(time.perf_counter()).split('.')[1]) 
            getcontext().prec = tempo
            pi = str(Decimal(3550000000000000000000000000000000000000000000000000000000) / Decimal(1130000000000000000000000000000000000000000000000000000000))
            limite = (numero2-1)
        
            limite_caracteres = int("-"+str(len(str(limite))))-1
        
            pi_aleatorio = int(pi[limite_caracteres:-1])
        return(pi_aleatorio)
        
        
            