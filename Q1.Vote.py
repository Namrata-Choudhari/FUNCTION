def eligible_for_vote(a):
    if a>=18:
        print("you are eligible")
    else:
        print("not eligible")
a=int(input("Enter the age:"))
eligible_for_vote(a)