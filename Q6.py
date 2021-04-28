# def calculator(num_x,num_y,operation):
#     if operation=="add":
#         print(num_x+num_y)
#     elif operation=="subtract":
#         print(num_x-num_y)
#     elif operation=="multiply":
#         print(num_x*num_y)
#     elif operation=="divide":
#         print(num_x/num_y)

# calculator(20,25,"add")
# calculator(40,3,"subtract")
# calculator(10,4,"multiply")
# calculator(40,4,"divide")

# num_x=int(input("enter a number"))
# num_y=int(input("enter a numx"))
# def calculator(num_x,num_y,operation):
#     if operation=="add":
#         print(num_x+num_y)
#     elif operation=="subtract":
#         print(num_x-num_y)
#     elif operation=="multiply":
#         print(num_x*num_y)
#     elif operation=="divide":
#         print(num_x/num_y)

# calculator(num_x,num_y,"add")


def list_change(a,b):
    i=0
    k=[]
    while i<len(a):
        j=0
        while j<len(b):
            if i==j:
                num=a[i]*b[j]
                k.append(num)
            j=j+1
        i=i+1
    print(k)


a=[5,10,50,20]
b=[2,20,3,5]
list_change(a,b)


