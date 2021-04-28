elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
def odd_even(num):
    i=0
    odd=[]
    even=[]
    while i<len(num):
        n=num[i]
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
        i=i+1
    print("odd numbers are:-",odd)
    print("even numbers are:-",even)


odd_even(elements)