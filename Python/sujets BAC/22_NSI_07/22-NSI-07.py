def conv_bin(n):
    b=[]
    bit=0
    while n!=0:
        b.append(n-2*(n//2))
        n=n//2
        bit+=1
    b.reverse()
    return (b,bit)


def tri_bulles(T):
    n = len(T)
    for i in range(n-2,0,-1):
        for j in range(i):
            print('i=',i,'  j=',j)
            if T[j] > T[i+1]:
                print('T[j]=',T[j],'  T[i+1]',T[i+1])
                temp = T[j]
                T[j] = T[i+1]
                T[j+1] = temp
                print(T)
    return T
