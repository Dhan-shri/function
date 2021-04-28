def total_sum(lst,num):
    i=0
    k=[]
    while i<len(lst):
        b=0
        while lst[i]>lst[b]:
            if lst[i]+lst[b]==num:
                k.append([lst[i],lst[b]])
            b=b+1
        i=i+1
    print(k)
n=[10,11,12,13,14,17,18,19]
total_sum(n,27)
