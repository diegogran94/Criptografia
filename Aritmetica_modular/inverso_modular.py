# -*- coding: utf-8 -*-

#Ejercicio 2 Practica 1

from euclides import euclides

def inverso_mod(a,b):
    """
    Esta función calcula el inverso modular de un número (a) módulo (b)
    haciendo uso del algoritmo extendido de Euclides
    
    Args:
        a(int): Número al que calcular el inverso
        b(int): Módulo en el que se trabaja
        
    Returns:
        int: Inverso de a modulo b
        -1: Si no existe inverso
        
    Example:
        >>inverso_modular(117,244)
        73
    """
    
    coefs = euclides(a,b)
    
    if(coefs[0]!=1):
        return -1 #no tiene inverso
    
    return coefs[1]%b
