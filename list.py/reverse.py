places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"] 
def reverse(string):
    i=0
    l=len(string)
    k=[]
    while i<len(string):
        n=string[i]
        n=string[l-i-1]
        k.append(n)
        i=i+1
    print(k)

reverse(places)


