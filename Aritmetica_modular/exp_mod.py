# -*- coding: utf-8 -*-


#Ejercicio 3

#Exponenciación modular

def exp_mod(a,b,n):
    """
    Esta función calcula a^b mod n
    
    Args:
        a(int): Base
        b(int): Exponente
        n(int): Módulo
        
    Returns:
        int: a^b mod n
        
    Example:
        >>exp_mod(3,3,10)
        7
    """

    prod=1
    
    while(b>0):
        if(b%2 == 1):
            b=(b-1)/2
            prod=(prod*a)%n
            
        else:
            b=b/2
            
        a=(a*a)%n
        
    return(prod)