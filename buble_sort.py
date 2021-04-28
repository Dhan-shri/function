def bubble_sort(num):
    i=0
    while i<len(num):
        j=0
        while j<len(num)-1:
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
            j=j+1
        i=i+1
    print(num)

lst=[2,3,4,6,7,1,9,5]
bubble_sort(lst)