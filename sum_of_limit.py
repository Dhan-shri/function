#Ek function likhiye jo ki ek limit naam ka parameter lega aur 0 se limit 
# tak ke beech ke number jo ki 3 aur 5 ke multiples hain unka sum print karega.jaisa ki niche dikhaya gya hai.

def komal(limit):
    i=0
    sum=0
    while i<=limit:
        if i%3==0 or i%5==0:
            sum=sum+i
        i=i+1
    print(sum)
num=int(input("enter a number"))
komal(num)
