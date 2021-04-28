num = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
def sec_max(lst):
    i=0
    k=lst[0]
    while i<len(lst):
        if lst[i]>k:
            k=lst[i]
        i=i+1
    lst.remove(k)
    j=0
    a=lst[0]
    while j<len(lst):
        if lst[j]>a:
            a=lst[j]
        j=j+1
    print(a)

sec_max(num)
      
    