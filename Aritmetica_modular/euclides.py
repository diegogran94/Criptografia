# -*- coding: utf-8 -*-

#Ejercicio 1 Practica 2

def euclides(a,b):
    """
    Esta función calcula el máximo común divisor de a y b además de los u,v
    tales que a*u+b*v=mcd(a,b)
    
    Args:
        a(int): Entero 1
        b(int): Entero 2
    Returns:
        int: mcd(a,b)
        int: u
        int: v
    Example:
        euclides(4864,3458)
        (38, 32, -45)
    """
    
    u1=1
    v1=0
    u2=0
    v2=1
    
    while(b!=0):
        q = a//b
        r = a%b
        
        a=b
        b=r
        
        u=u1-q*u2
        v=v1-q*v2
        u1=u2
        u2=u
        v1=v2
        v2=v
        
    return(a,u1,v1)