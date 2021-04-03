def arrange(a):
    i=min(a)+1
    count=0
    while i<max(a):
        if i not in a:
            count+=1
        i+=1
    print(count)
arrange([6,11,8])