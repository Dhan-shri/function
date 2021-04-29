#Ek function define karo jo ki input me 2 strings lega aur dono strings me se jiski length jyaada hogi use print karega 
# aur agar dono strings ki length equal hui to dono ko line by line print karega .

def string(a,b):
    if len(a)>len(b):
        print(a)
    elif len(a)<len(b):
        print(b)
    else:
        print(a)
        print(b)

string("komal","dhanshri")

string("dhanu","komal")