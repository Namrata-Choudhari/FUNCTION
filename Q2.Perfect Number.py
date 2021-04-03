def perfect_Number(a):
    i=1
    sum=1
    while i<a:
        if a%i==0:
            sum=sum*i
        i+=1
    print(sum)
    if sum==a:
        print("It is perfect Number")
    else:
        print("It is not perfect Number")
a=int(input("Enter the Number:"))
perfect_Number(a)
