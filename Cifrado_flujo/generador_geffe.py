# -*- coding: utf-8 -*-

#Ejercicio 4

from lfsr import lfsr

def generador_geffe(func1, sem1, func2, sem2, func3, sem3, l):

    x1 = lfsr(func1,sem1,l)
    x2 = lfsr(func2,sem2,l)
    x3 = lfsr(func3,sem3,l)

    s = []

    for i in range(0,l):
        p1 = x1[i]*x2[i]
        p2 = x2[i]*x3[i]
        p3 = x3[i]

        f = p1 ^ p2 ^ p3

        s.append(f)

    return s

def cifrado(msg, func1, sem1, func2, sem2, func3, sem3):
    
    k = generador_geffe(func1, sem1, func2, sem2, func3, sem3, len(msg))
    
    msg_cif = ""
    for i in range(len(msg)):
        msg_cif+=chr(ord(msg[i])^k[i])
    
    return msg_cif, k

def descifrado(msg_cif, k):
    
    msg = ""
    for i in range(len(msg_cif)):
        msg+=chr(ord(msg_cif[i])^k[i])
        
    return msg
    
    
if __name__ == '__main__':
    
    mensaje = "Sólo sé que no sé nada"
    print("Mensaje a cifrar:",mensaje)
    a1 = cifrado(mensaje, [0,1,0,1],[1,1,1,1],[1,1,1,0],[1,0,1,1],[1,1,0,0],[0,1,1,1])
    print("Mensaje cifrado:",a1[0])
    a2 = descifrado(a1[0],a1[1])
    print("Mensaje descifrado:",a2)
    
    

