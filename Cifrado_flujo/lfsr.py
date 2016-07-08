# -*- coding: utf-8 -*-

#Ejercicio 2

from golomb import golomb


def lfsr(pol, semilla, lon_salida):

    secuencia = semilla
    L = len(semilla)

    for j in range(0,lon_salida-L):
        sj=0
        for i in range(0,len(pol)):
            aux = pol[i] & secuencia[j+i]
            sj = sj ^ aux
        secuencia.append(sj)

    return secuencia

if __name__ == '__main__':
    
    #Con un polinomio reducible el periodo es dependiente de la semilla
    print('LFSR usando un polinomio reducible')
    print(lfsr([0,1,1,1],[1,0,1,0],15))
    print(lfsr([0,1,1,1],[1,1,1,1],15))
    
    #Introduciendo un polinomio irreducible el periodo de la semilla es independiente de esta. 
    s1 = lfsr([0,0,1,1],[1,0,1,0],15)
    s2 = lfsr([0,0,1,1],[1,1,1,1],15)
    print('\nLFSR usando un polinomio irreducible')
    print(s1)
    print(s2)
    
    print('\nLFSR usando un polinomio primitivo')
    s3 = lfsr([1,0,0,1],[1,1,1,1],(2**4)-1)
    print(s3)
    print('¿Cumple esta secuencia los postulados de Golomb?')
    golomb(s3)