# -*- coding: utf-8 -*-

#Práctica 1 Criptografía
#Aritmetica modular


import timeit

from euclides import euclides
from inverso_modular import inverso_mod
from exp_mod import exp_mod
from primo import es_primo
from log_dis import log_dis
from sqrt_mod import sqrt_mod
from sqrt_mod_2 import sqrt_mod_2
from pollard import pollard
from fermat import fermat

#Numero de ejecuciones
n_ejec=100

a=4864
b=3458

print("Ejercicio 1. Algoritmo extendido de Euclides")
print("Parámetros: a=",a," b=",b)
print("Solucion: ",euclides(a,b))
t = timeit.Timer(lambda: euclides(a,b))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

a=117
b=244

print("Ejercicio 2. Inverso modular")
print("Parámetros: a=",a," b=",b)
print("Solucion: ",inverso_mod(a,b))
t = timeit.Timer(lambda: inverso_mod(a,b))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

a=5
b=596
n=1234

print("Ejercicio 3. Exponenciación modular")
print("Parámetros: a=",a," b=",b,"n=",n)
print("Solucion: ",exp_mod(a,b,n))
t = timeit.Timer(lambda: exp_mod(a,b,n))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

a=123456789101119

print("Ejercicio 4. Miller-Rabbin")
print("Parámetros: a=",a)
print("Solucion: ",es_primo(a))
t = timeit.Timer(lambda: es_primo(a))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

n=113
a=3
b=57

print("Ejercicio 5. Paso enano-paso Gigante")
print("Parámetros: a=",a," b=",b,"n=",n)
print("Solucion: ",log_dis(n,a,b))
t = timeit.Timer(lambda: log_dis(a,b,n))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

a=319
p=353

print("Ejercicio 6. Raiz cuadrada modular")
print("Parámetros: a=",a," b=",b,"n=",n)
print("Solucion: ",sqrt_mod(a,p))
t = timeit.Timer(lambda: sqrt_mod(a,p))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

a=132
p=17
q=29
n=493

print("Ejercicio 6. Raiz cuadrada modular pro")
print("Parámetros: a=",a," p=",p,"q=",q," n=",n)
print("Solucion: ",sqrt_mod_2(a,p,q,n))
t = timeit.Timer(lambda: sqrt_mod_2(a,p,q,n))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

n=5959

print("Ejercicio 7. Metodo de Fermat")
print("Parámetros: n=",n)
print("Solucion: ",fermat(n))
t = timeit.Timer(lambda: fermat(n))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")

n=455459

print("Ejercicio 7. Rho de Pollard")
print("Parámetros: n=",n)
print("Solucion: ",pollard(n))
t = timeit.Timer(lambda: pollard(n))
print("Tiempo de ejecución medio(",n_ejec,"ejecuciones): ",t.timeit(n_ejec)/n_ejec)
print("---------------------------------------------------------")


