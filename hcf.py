#Highest common factor



# def hcf(x, y):  
#     if x > y:  
#         smaller = y  
#     else:  
#         smaller = x  
#     for i in range(1,smaller + 1):  
#         if((x % i == 0) and (y % i == 0)):  
#             hcf = i  
#     return hcf  
    
# num1 = int(input("Enter first number: "))  
# num2 = int(input("Enter second number: "))  
# print("The H.C.F. of", num1,"and", num2,"is", hcf(num1, num2))  

def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    i=1
    while i<smaller+1:
        if (x%i)==0 and y%i==0:
            hcf =i
        i=i+1
    print(hcf)

n=int(input("enter first number:-"))
num=int(input("enter second number:-"))
hcf(n,num)