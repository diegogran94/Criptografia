# -*- coding: utf-8 -*-

# JACOBI(a,n)
# INPUT: an odd integer n ≥ 3, and an integer a, 0 ≤ a < n.
# OUTPUT: the Jacobi symbol (a/n) (and hence the Legendre symbol when n is prime).
#     1. If a = 0 then return(0).
#     2. If a = 1 then return(1).
#     3. Write a = 2 e a 1 , where a 1 is odd.
#     4. If e is even then set s←1. Otherwise set s←1 if n ≡ 1 or 7 (mod 8), or set s← − 1
#     if n ≡ 3 or 5 (mod 8).
#     5. If n ≡ 3 (mod 4) and a 1 ≡ 3 (mod 4) then set s← − s.
#     6. Set n 1 ←n mod a 1 .
#     7. If a 1 = 1 then return(s); otherwise return(s · JACOBI(n 1 ,a 1 )).

def jacobi(a,n):
    """
    Función que calcula el simbolo de jacobi (a/n)
    
    Args:
        n(int): Entero impar >= 3
        a(int): Entero 0 <= a < n
        
    Returns:
        int: Simbolo de Jacobi (Simbolo de Legendre si n es primo)
    
    Examples:
    
    jacobi(158,235)
    -1
    
    jacobi(2,235)
    -1
    
    jacobi(5,299)
    1
    
    jacobi(646,809)
    -1
    """

    #Comprobar condiciones iniciales

    if a==0:
        return 0
    elif a==1:
        return 1

    e=0
    a1=a
    while a1%2==0:
        e=e+1
        a1=a1//2

    if e%2==0:#if e is even
        s=1
    else:
        if n%8==1 or n%8==7:
            s=1
        elif n%8==3 or n%8==5:
            s=-1

    if n%4==3 and a1%4==3:
        s=-s

    n1=n%a1

    if a1==1:
        return s
    else:
        return (s*jacobi(n1,a1))
