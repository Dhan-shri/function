def expand(num):
    digit=str(num)
    i=0
    l=len(digit)
    k=l-1
    while i<len(digit):
        code=int(digit[i])
        e=code*(10**k)
        print(e,end="")
        if i!=len(digit)-1:
            print("+",end="")
        i=i+1
        k=k-1

expand(567)
