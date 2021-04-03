def add_numbers(num1,num2):
    print(num1+num2)
num1 = 56
num2 = 12
add_numbers(num1,num2)


# def add_numbers_list(a,b):
#     i=0
#     while i<len(a):
#         c=a[i]+b[i]
#         i+=1
#         print(c)
# add_numbers_list([50,60,10],[10,20,13])

def add_numbers_list(a,b):
    for i in range(0,len(a)):
        add_numbers(a[i],b[i])
add_numbers_list([50,60,10],[10,20,13])
