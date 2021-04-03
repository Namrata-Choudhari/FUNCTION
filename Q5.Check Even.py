def check_numbers(a,b):
    if a%2==0 and b%2==0:
        print("dono number even hai")
    else:
        print("Dono number even nahi hai")
# a=int(input("Enter the number:"))
# b=int(input("Enter the number:"))
# check_numbers(5,6)

def check_numbers_list(a,b):
    i=0
    for i in range(i,len(a)):
        check_numbers(a[i],b[i])
check_numbers_list([2,6,18,10,3,75],[6,19,24,12,3,87])