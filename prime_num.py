def perfect(num):
    i = 1
    sum = 0
# n = int(input("Enter a number: "))
    while(i <= num /2 ) :
        if (num % i == 0) :
            sum=sum+ i
        i =i+ 1
    if sum == num :
        print(num,"is a perfect number")
    else :
        print(num,"is not a perfect number")

perfect(8)

    