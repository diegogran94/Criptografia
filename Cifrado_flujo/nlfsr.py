# -*- coding: utf-8 -*-

#Ejercicio 3


def nlfsr(pol, semilla, lon_salida):

    secuencia = semilla
    L = len(semilla)
    n_vars = len(pol[0])

    for i in range(0,lon_salida-L):
        a=0
        for j in range(0,len(pol)):
            b=0
            for k in range(0,n_vars):
                b ^= pol[j][k] & secuencia[k+i]
            a ^= b
        secuencia.append(a)

    return secuencia

if __name__ == '__main__':
    #Ejemplo propuesto en el ejercicio #xyz+xy+t+1
    print(nlfsr([[1,1,1,0],[1,1,0,0],[0,0,0,1],[0,0,0,0]],[1,0,1,1],15))