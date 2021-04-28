elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
def odd_even_sum(num):
    i=0
    s=0
    sum=0
    while i<len(num):
        n=num[i]
        if n%2==0:
            sum=sum+n
        else:
            s=s+n
        i=i+1
    print("sum of even numbers",sum)
    print("sum of odd numbers",s)

odd_even_sum(elements)