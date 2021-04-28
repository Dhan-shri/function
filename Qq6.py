# def drivers_speed(speed):
#     i=1
#     while i>0:
#         if speed<70:
#             print("ok")
#         if speed>70:
#             point=1
#             while point<12:   
#                 if speed>=70+i:
#                     print("point:",point)
#                 if point>12:
#                     print("license suspended")
#                 point=point+1
#         i=i+5

# drivers_speed(70)



def drivers_speed(speed):
    if range_of_speed<=70:
        print("ok")
    elif range_of_speed>70:
        a=speed-70
        print(a)
        b=a%5
        if b==0:
            print("point:",a//5)
        if a>12:
            print("licence suspended")
        
range_of_speed=int(input("enter a speed"))
drivers_speed(range_of_speed)
        