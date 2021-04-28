# Least Common Multiple(LCM) is a method to find the smallest common multiple between any two or more numbers. 


# def lcm(x,y):
#     if x>y:
#         greater=x
#     else:
#         greater=y
#     i=2
#     while i<greater*2+1:
#         if i%x==0 and i%y==0:
#             l=i
#             break
#         i=i+1
#     print(l)

# n=int(input("enter first number:-"))
# num=int(input("enter second number:-"))

# lcm(n,num)

def lcm(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    i=1
    while i<=x*y:
        if (i%x)==0 and i%x==0:
            lcm=i
        i=i+1
    print(lcm)

n=int(input("enter first number:-"))
num=int(input("enter second number:-"))
lcm(n,num)