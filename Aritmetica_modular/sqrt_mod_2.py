# -*- coding: utf-8 -*-

from sqrt_mod import sqrt_mod
from euclides import euclides

def sqrt_mod_2(a,p,q,n):
    r=sqrt_mod(a,p)
    s=sqrt_mod(a,q)
        
    aux=euclides(p,q)#Salida de euclides=(mcd,u,v)
    c=aux[1]
    d=aux[2]
    
    x=(r*d*q + s*c*p)%n
    y=(r*d*q - s*c*p)%n
    
    return(x,-x%n,y,-y%n)
    