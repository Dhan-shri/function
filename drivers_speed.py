#Ek function define kijiye jo ki drivers ki speed check karega.


def drivers_speed(speed):
    if range_of_speed<=70:
        print("ok")
    elif range_of_speed>70:
        a=speed-70
        print("speed difference:-",a)
        b=a%5
        if b==0:
            print("point:",a//5)
        if a>12:
            print("licence suspended")
        
range_of_speed=int(input("enter a speed"))
drivers_speed(range_of_speed)
        