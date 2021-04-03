def string(a,b):
    if len(a)>len(b):
        print(a)
    elif len(b)>len(a):
        print(b)
    elif len(a)==len(b):
        print(a,b)
a=input("Enter the Name:")
b=input("Enter the Name:")
string(a,b)