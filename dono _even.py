# def check_numbers(a,b):
#     if a%2==0 and b%2==0:
#         print("dono even hai")
#     else:
#         print("dono even nahi hai")

# num=4
# num2=8
# check_numbers(num, num2)


def check_number_list(a,b):
    i=0
    j=0
    while i<len(a):
        while j<len(b):
            if (a[i] and b[i])%2==0:
                print("dono even hai")
            else:
                print("dono even nahi hai")  
            j=j+1
            break
        i=i+1          

a=[2,6,18,10,3,75]
b=[6,19,24,12,3,87]
check_number_list(a,b)







