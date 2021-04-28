def binary(num):
    l=len(num)
    i=0
    sum=0
    while i<l:
        n=num[l-i-1]
        sum=sum+n*(2**i)
        i=i+1
    print(sum)

num=[1,0,0,1,1,1,1,1]
binary(num)

# def binary(num):
#     n=str(num)
#     l=len(n)
#     j=0
#     i=l
#     sum=0
#     while j<len(n):
#         k=int(n[j])
#         sum=sum+k*(2**i)
#         j=j+1
#         i=i-1
#     print(sum)

# binary(10011111)
        