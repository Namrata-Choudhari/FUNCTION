def speed(a):
    if a<=70:
        print("ok")
    else:
        speed=70
        count=0
        while speed<a:
            count=count+1
            speed+=1
        a=count//5
        if a>12:
            return "License Suspended"
        print(a)
a=int(input("Enter the Number:"))
print(speed(a))