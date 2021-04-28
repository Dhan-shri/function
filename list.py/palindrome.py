# name=[ 'n', 'i', 't', 'i', 'n' ] 
# def palindrome(string):
#     i=0
#     k=[]
#     l=len(string)
#     while i<len(name):
#         n=string[i]
#         num=string[l-i-1]
#         k.append(num)
#         i=i+1
#     if k==string:
#         print("it is palindrom")
#     else:
#         print("it is not a palindrome")

# palindrome(name)
        
def palindrome(num):
    n=str(num)
    i=0
    l=len(n)
    while i<len(n):
        k=n[l-i-1]
        a=print(k)
        i=i+1
        b=int(a)
    if b==num:
        print("it is palindrome")
    else:
        print("it is not palindrome")
    
palindrome(12321)


