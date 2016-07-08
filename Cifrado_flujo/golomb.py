# -*- coding: utf-8 -*-

#Ejercicio 1


import copy

def golomb(secuencia):

    #Primer postulado: #0 == #1

    ceros = unos = 0
    for i in secuencia:
        if i == 0:
            ceros+=1
        if i == 1:
            unos+=1

    if(abs(ceros-unos) > 1):
        print("No cumple el primer postulado")
        return False

    print("Cumple el primer postulado")

    #Segundo postulado: #rachas de long 1 = doble #rachas lon 2 ...

    rachas=[0] * len(secuencia)#Inicializar lista a 0
    lon_racha=1

    for i in range(0,len(secuencia)):
        if(i < len(secuencia)-1):
            if(secuencia[i+1]==secuencia[i]):
                lon_racha+=1
            else:
                rachas[lon_racha]+=1
                lon_racha=1
        else:
            rachas[lon_racha]+=1

    #print("Rachas",rachas)

    for i in range(1,(len(rachas)-1)):
        if(i<(len(rachas)-2)):
            if(rachas[i+1]!=0 and rachas[i+2]!=0):
                if(rachas[i]!=rachas[i+1]*2):
                    print("No cumple el segundo postulado")
                    return False
        else:
            if(rachas[i]<rachas[i+1]):
                print("No cumple el segundo postulado")
                return False


    print("Cumple el segundo postulado")

    #Tercer postulado: Dis hamming constante

    copia_secuencia = copy.copy(secuencia)
    dist_hamming=0
    dist_hamming_anterior=0

    for i in range(1,len(secuencia)):
        #Desplazar secuencia
        aux = copia_secuencia.pop(0)
        copia_secuencia.append(aux)
        #print(copia_secuencia)

        for j in range(0,len(secuencia)):
            if(secuencia[j]!=copia_secuencia[j]):
                dist_hamming+=1

        if(i==1):#En la primera iteracion ....
            dist_hamming_anterior=dist_hamming

        if(dist_hamming!=dist_hamming_anterior):
            print("No cumple el tercer postulado")
            return False

        dist_hamming=0

    print("Cumple el tercer postulado")
    return True
    

if __name__ == '__main__':
    print("¿La secuencia 0,0,1,1,1,0,1 cumple los postulados de Golomb?")
    print(golomb([0,0,1,1,1,0,1]))
