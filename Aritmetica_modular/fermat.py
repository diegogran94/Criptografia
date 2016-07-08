# -*- coding: utf-8 -*-

import math

def fermat(n):
    """
    Esta función factoriza un numero impar como diferencia de cuadrados según el
    método de Fermat (n = a^2 - b^2)
    
    Args:
        n(int): Entero impar
        
    Return:
        a,b(int): Factores (a*b = n)
        
    Examples:
        >>fermat(5959)
        (59, 101)
    """
    
    a=math.ceil(math.sqrt(n))
    
    bcuad = a*a-n
   
    b = math.sqrt(bcuad)

    while not (b).is_integer():
        a+=1
        bcuad = a*a-n
        b = math.sqrt(bcuad)
    
    return (int(a-b),int(a+b))