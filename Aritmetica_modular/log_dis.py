# -*- coding: utf-8 -*-

#Ejemplo en los apuntes:
#log_dis(23,5,8)
#6

#Ejemplo del libro:
#log_dis(113,3,57)
#100

import math

from exp_mod import exp_mod

def log_dis(n, alpha, beta):
    """
    Función que calcula logartimos discretos mediante el algoritmo 
    paso enano-paso gigante
    
    Args:
        n(int): Orden del grupo cíclico
        alpha(int): Base del logaritmo
        beta(int): Elemento
        
    Return:
        int: Logaritmo discreto en base alpha de beta módulo n
        
    Examples:
        
        >>log_dis(23,5,8)
        6

        >>log_dis(113,3,57)
        100
    """

    s=int(math.ceil(math.sqrt(n)))
    l1=[(exp_mod(alpha,i*s,n))%n for i in range(1,s+1)]
    l2=[(beta*exp_mod(alpha,j,n))%n for j in range(s)]    
    
    #Buscamos coincidencias en las listas y obtenemos los indices del elemento comun
    for i in l1:
        for j in l2:
            if i==j:
                p1 = l1.index(i)
                p2 = l2.index(j)
                break
            
    return ((p1+1)*s - p2) % n
            