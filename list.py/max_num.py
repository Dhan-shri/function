numbers=[50, 40, 23, 70, 56, 12, 90, 7]
def max_num(num):
    i=0
    c=num[0]
    while i<len(num):
        n=num[i]
        if n>c:
            c=n
        i=i+1
    print(c)


max_num(numbers)