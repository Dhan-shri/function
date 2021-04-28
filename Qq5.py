def komal(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
num=int(input("enter a number"))
komal(num)
