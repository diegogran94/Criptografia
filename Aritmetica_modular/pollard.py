# -*- coding: utf-8 -*-

#INPUT: a composite integer n that is not a prime power.
#OUTPUT: a non-trivial factor d of n.
#1. Set a←2, b←2.
#2. For i = 1, 2, . . . do the following:
#2.1 Compute a←a2 + 1 mod n, b←b2 + 1 mod n, b←b2 + 1 mod n.
#2.2 Compute d = gcd(a − b, n).
#2.3 If 1 < d < n then return(d) and terminate with success.
#2.4 If d = n then terminate the algorithm with failure (see Note 3.12).

from euclides import euclides

def pollard(n):
    """
    Función que devuelve los factores no triviales de un entero dado mediante
    el algoritmo rho de Pollard
    
    Args:
        n(int): Entero
    
    Returns:
        int: Uno de los factores de n
        -1: Si no se puede factorizar
        
    Example:
        pollard(455459)
        743
    """
    
    a = b = 2
    
    for i in range(1000):
        a = ((a*a)+1)%n
        b = ((b*b)+1)%n
        b = ((b*b)+1)%n
        c = a-b
        aux = euclides(c,n)
        d = aux[0]#mcd(a-b,n)
        
        if(d>1 and d<n):
            return d
        
        if(d==n):
            return -1
            
    return -1