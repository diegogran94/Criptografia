# -*- coding: utf-8 -*-

# --Miller-Rabin algorithm--
#
# Input: n > 2, an odd integer to be tested for primality;
#        k, a parameter that determines the accuracy of the test
# Output: composite if n is composite, otherwise probably prime
# write n − 1 as 2s·d with d odd by factoring powers of 2 from n − 1
# LOOP: repeat k times:
#    pick a randomly in the range [2, n − 1]
#    x ← a^d mod n
#    if x = 1 or x = n − 1 then do next LOOP
#    for r = 1 .. s − 1
#       x ← x^2 mod n
#       if x = 1 then return composite
#       if x = n − 1 then do next LOOP
#    return composite
# return probably prime

import random

from exp_mod import exp_mod

def es_primo(p,k=7):
    """
    Esta función comprueba si el número dado es primo o no mediante el algoritmo de Miller-Rabin.

    Args:
        p(int): Número el cual comprobaremos si es primo.
        k(int): Número de iteraciones del algoritmo. Por defecto se incializa a 7.

    Returns:
        bool: True si es primo, False si no lo es.

    Example:
        >>es_primo(123456789101119)
        True
    """
    fin_bucle=True

    if(p in [2,3,5,7,11]):
        return True
    elif(p<11):
        return False#Si no esta contenido en la lista anterior y es menor que el último, no es primo
    if(p%2 != 0):
        s=0
        d=p-1
        while d%2==0:
            s=s+1
            d=d//2

        for i in range(0,k):
            a = random.randint(2,p-1)
            x = exp_mod(a,d,p)
            if(x!=1 and x!=p-1):
                for r in range(1,s):
                    x = exp_mod(x,2,p)
                    if(x%p==1):
                        return False #Es par
                    elif(x%p==p-1):
                        fin_bucle=False
                        break
                if fin_bucle:
                    return False#No encuentra un -1
        return True #Probablemente primo
    else:
        return False #Porque es par

print(es_primo(123456789101119))
