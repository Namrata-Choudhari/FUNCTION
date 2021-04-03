# def calculator(a,b,c):
#     if c=="add":
#         return("addition",a+b)
#     elif c=="sub":
#         return("subtract",a-b)
#     elif c=="mul":
#         return("multiply",a*b)
#     elif c=="div":
#         return("division",a/b)
# print(calculator(20,25,"add"))
# print(calculator(40,3,"sub"))
# print(calculator(10,4,"mul"))
# print(calculator(40,4,"div"))
# calculator("a","b","c")

# def calculator(a,b):
#     print("add_result",a+b)
#     print("subtract_result",a-b)
#     print("multiply_result",a*b)
#     print("divide_result",a/b)
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# calculator(a,b)

def list_change(a,b):
    i=0
    c=[]
    for i in range(i,len(a)):
        d=a[i]*b[i]
        c.append(d)
    print(c)
list_change([5, 10, 50, 20], [2, 20, 3, 5]) 