def one_list(lst,lst1):
    i=0
    k=[]
    while i<len(lst):
        num=lst[i]
        if num  not in lst1:
            k.append(num)  
        i=i+1
    print(k)

list1 = [1,2,3,4,5,6]
list2 = [2,3,1,0,6,7] 
one_list(list1,list2)