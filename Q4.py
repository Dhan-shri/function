# def add_numbers(a,b):
#     print(a+b)

# num1=56
# num2=12
# add_numbers(num1,num2)

def list1(a,b):
    i=0
    j=0
    while i<len(a):
        num=a[i]
        while j<len(b):
            num1=b[j]
            print(num+num1)
            j=j+1
            break
        i=i+1



a=[10,20,30]
b=[20,30,40]
list1(a,b)
