def sum(limit):
    i=0
    s=0
    while i<=limit:
        if i%3==0 or i%5==0:
            s=s+i
        i+=1
    print(s)
limit=int(input("Enter the Number:"))
sum(limit)