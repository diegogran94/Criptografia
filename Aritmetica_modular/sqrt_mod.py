# -*- coding: utf-8 -*-

from jacobi import jacobi
from exp_mod import exp_mod
from inverso_modular import inverso_mod

def sqrt_mod(a,p):
    """
    Calcula la raiz cuadrada modular de a módulo p
    
    Args:
        a(int): Entero
        p(int): Entero primo
        
    Returns:
        r(int): Raiz de a modulo p        
        
    Examples:
        sqrt_mod(319,353)
        242
    """
    
    if jacobi(a,p) == -1:
        return -1
        
        
    n=1
    
    while jacobi(n,p) != -1:
        n+=1
        
    
    u=0
    s=p-1
    while s%2==0:
        u=u+1
        s=s//2
    print(u,s);
        
    if u == 1:
        r=exp_mod(a,(p+1)/4,p)
    elif u >= 2:
        r=exp_mod(a,(s+1)/2,p)
        b=exp_mod(n,s,p)
        j=0
        
        while j<= u-2:
            base = (inverso_mod(a,p)*r*r)%p
            exp = exp_mod(2,u-2-j,p)  
            if exp_mod(base,exp,p) == (-1%p):
                r=(r*b)%p
            b=(b*b)%p
            j+=1
            
      
    return r
        
    
