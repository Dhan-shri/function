#Ek function likho jo ki ek argument le jo number ho or dictionary return karega jisme keys 1 se lekar argument ke number tak 
# hogi aur values unke squares honge.jaisa ki niche dikhaya gaya hai.

def square(num):
    i=1
    k={}
    while i<=num:
        k[i]=i**2
        i=i+1
    print(k)


square(20)

