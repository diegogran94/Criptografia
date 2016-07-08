# -*- coding: utf-8 -*-

#Ejercicio 5

def ber_mas(seq):

    for i in range (0,len(seq)):
        if(seq[i] == 1):
            k=i
            break

    f = [0]*len(seq)
    f[0]=1
    f[k+1]=1

    g = [0]*len(seq)
    g[0]=1

    (l,a,b,r) = (k+1,k,0,k+1)

    aux = []

    #print ("| r | l | a | b |    f    |    g    | d | 2l>r |    aux    |")
    while(r<len(seq)):
        d = 0
        for i in range(0,l+1):
            d ^= f[i]*seq[i+r-l]
        if (d==0):
            b+=1
        if (d == 1):
            if (2*l>r):
                for i in range(0,l+1):
                    f[i]=f[i] ^ g[i+(b-a)]
                b+=1
            else:
                aux = f[:]
                for i in range(0,r+l):
                    f[i]=aux[i+(a-b)] ^ g[i]
                l = r-l+1
                g = aux[:]
                a=b
                b=r-l+1
        r+=1
        #print (r,l,a,b,f,g,d,2*l>r,aux)


    return l,f

if __name__ == '__main__':
    
    print(ber_mas([1,0,1,1,1,1,0,0,0,1,0,0,1,1]))
