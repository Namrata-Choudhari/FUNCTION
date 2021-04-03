# print ("NavGurukul")
# def say_hello():
#     print ("Hello!")
#     print ("Aap kaise ho?")
# say_hello()
# print ("Python is awesome")
# say_hello()
# print ("Hello…")
# say_hello()
# print("namrata")

# #length
# name_list=["fiza","shivam","imtiyaz","deepanshu","rahman"]
# print(len(name_list))

# def definition_say_hello():
#     print("Navgurukul")
#     print("Navgururkul mei humein apni learning ki responsibility leni padti hai")
# definition_say_hello()
# print("navgurukul mei hum sab logo ko ek tarah se treat karte hai.")
# definition_say_hello()

# def function_say_bye():
#     print("Aapka mil ke maza aaya")
#     print("Bye bye")
# function_say_bye()
# function_say_bye()
# print("Python ka bahot jagah hota hai")
# function_say_bye()
# function_say_bye()

# def definition_hello_again():
#     print("Firse Hello:)")
#     print("Aap kaise ho?")
# definition_hello_again()

# def ask_question():
#     print("ek baar")
# ask_question()
# ask_question()
# ask_question()
# ask_question()
# ask_question()

# def ask_question():
#     print("ek baar")
# i=0
# while i<=100:
#     ask_question()
#     i+=1

# #predefine function
# n=[3,5,7,34,2,89,2,5]
# print(max(n))

# n=[1,2,3,4,5]
# print(sum(n))

# #decending order
# unorder_list=[6,8,4,3,9,56,0,34,7,15]
# unorder_list.sort(reverse=True)
# print(unorder_list)

# #accending order
# unorder_list=[6,8,4,3,9,56,0,34,7,15]
# unorder_list.sort()
# print(unorder_list)

# # Reverse list
# reverse_list=["z","a","a","b","e","m","a","r","d"]
# reverse_list.reverse()
# print(reverse_list)

# # minimum
# list=[8,6,4,8,4,50,2,7]
# print(min(list))

# # Debugging Question
# def sum():
#     print(12+13)
# sum()

# def welcome():
#     print("Welcome to function")
# welcome()

# def isEven():
#     if(12%2==0):
#         print("Even Number")
#     else:
#         print("Old Number")
# isEven() 

# def greet(*names):
#     for name in names:
#         print("Welcome", name)


# greet("Rinki", "Vishal", "Kartik", "Bijender") 

# def info(name, age ="16"):
#        print(name + " is " + age + " years old")

# info("Sonu")
# info("Sana", "17")
# info("Umesh", "18") 

# def studentDetails(name,currentMilestone,mentorName):
#     print("Hello " , name, "your" , currentMilestone, "concept " , "is clear with the help of ", mentorName)
# studentDetails("Nilam","loop","Namrata") 

# def say_hello(name):
#     print ("Hello ", name)
#     print ("Aap kaise ho?")
# say_hello("Aatif")
# say_hello("namrata")

# def add_numbers(number1, number2):
#     print ("Main do numbers ko add karunga.")
#     print (number1 + number2)
# add_numbers(120, 50)
# num_x = "134"
# name = "rinki"
# add_numbers(num_x, name) 

# def say_hello_people(name_x, name_y, name_z, name_a):
#     print ("Namaste ", name_x) # hindi mein
#     print ("Alah hafiz ", name_y) # urdu mein
#     print ("Bonjour ", name_z) # french mein
#     print ("Hello ", name_a) # english mein
# say_hello_people("Imitiyaz", "Rishabh", "Rahul", "Vidya")
# say_hello_people("Steve", "Saswata", "Shakrundin", "Rajeev") 

# def icecream(*flavours):
#     for flavour in flavours:
#         print("i love"+flavour)
# icecream("chocolate", "butterscotch","vanilla","strawberry") 

# def attendance(name,status="absent"):
#     print(name,"is",status," today")

# attendance("kartik","present")
# attendance("sonu")
# attendance("vishal","present")
# attendance("umesh") 

# # return value
# def add_numbers(number_x, number_y):
#     number_sum = number_x + number_y
#     return number_sum
# sum1 = add_numbers(20, 40)
# print (sum1)
# sum2 = add_numbers(560, 23)
# a = 1234
# b = 12
# sum3 = add_numbers(a, b)
# print (sum2)
# print (sum3)
# number_a = add_numbers(20, 40) / add_numbers(5, 1)
# print (number_a) 

# def add_numbers_print(number_x, number_y):
#     number_sum = number_x + number_y
#     print (number_sum)
# sum4 = add_numbers_print(4, 5)
# print (sum4)
# print (type(sum4)) 
 
# def add_numbers_more(number_x, number_y):
#     number_sum = number_x + number_y
#     print ("Hello from NavGurukul ;)")
#     return number_sum
#     number_sum = number_x + number_x
#     print ("Kya main yahan tak pahunchunga?")
#     return number_sum

# sum6 = add_numbers_more(100, 20) 

# def menu(day):
#     if day == "monday":
#         return "Butter Chicken"
#     elif day == "tuesday":
#         return "Mutton Chaap"
#     else:
#         return "Chole Bhature"

#     print ("Kya main print ho payungi? :-(")

# mon_menu = menu("monday")
# print (mon_menu)
# tues_menu = menu("tuesday")
# print (tues_menu)
# fri_menu = menu("friday")
# print (fri_menu) 

# def menu(day):
#     if day == "monday":
#         food = "Butter Chicken"
#     elif day == "tuesday":
#         food = "Mutton Chaap"
#     else:
#         food = "Chole Bhature"
#     print ("Kya main print ho payungi? :-(")
#     return food
#     print ("Lekin main toh pakka nahi print hounga :'(")
# print(menu("monday")) 

# # inner function
# def f1():
#     s = "I Love Navgurukul"
#     def f2():
#        print(s)
#     f2()
# f1()

# def first_function():
#     s = 'I love India'
#     def second_function():
#         print(s)     
#     second_function()
# first_function()  

# def first_function():
#     s = 'I love India'
#     def second_function():
#         s = "MY NAME IS JACK"
#         print(s)     
#     second_function()
#     print(s)    
# first_function() 

# def add(param1, param2):
#     return param1+param2
# print(add(1,2))

# def centuryFromYear(year):
    
#     if year%100==0:
#         print(int(year/100))
#     else:
#         print(int(year/100+1))
# year=int(input("Enter the Year:"))    
# centuryFromYear(year)

# def list(a):
#     print(a)
# i=0
# s=[]
# while i<10:
#     a=int(input("enter the number:"))
#     s.append(a)
#     i+=1
# print(s) 
# list(a)

# def arrange(a):
#     i=min(a)+1
#     count=0
#     while i<max(a):
#         if i not in a:
#             count+=1
#         i+=1
#     print(count)
# arrange([6,11,8])