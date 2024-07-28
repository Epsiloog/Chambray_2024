def decTobr(n,b):
    assert(b>1 and b<17)
    signes=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    if n==0:
        return("")
    else:
        return decTobr(n//b,b) + signes[n%b]