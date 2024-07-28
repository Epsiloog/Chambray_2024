def multiplication(n1,n2):
    assert(type(n1)==int and type(n2)==int)

    def sum_loop(n1,n2):
        p1=n1
        for i in range (n2-1):
            n1+=p1
        return n1

    if n1<0 and n2<0:
        n1=abs(n1) ; n2=abs(n2)
        print(sum_loop(n1,n2))

    elif n1>0 and n2>0:
        print(sum_loop(n1,n2))

    elif n1==0 or n2==0:
        return 0

    else:
        n1=abs(n1) ; n2=abs(n2)
        print(-sum_loop(n1,n2))


def chercher(T,n,i,j):
    if i < 0 or j>=len(T) :
        print("Erreur")
        return None
    if i > j :
        return None
    m = (i+j) // len(T)
    if T[m] < n :
        return chercher(T, n, m+1 ,j)
    elif T[m]>n :
        return chercher(T, n, i, m-1)
    else :
        return m
