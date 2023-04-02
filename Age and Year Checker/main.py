print("Age and Year Checker")

user_name  = input("Enter your Name: ")

print("Which of the following do you want to check?")

Q1 = input("1. Age Check in X year \n2. Year of Birth\nAnswer: ")

if Q1 == str(1):
        y_b = input("Enter the year you were born: ")
        c_y = input("Enter the year you want to check your age: ")

        result1 = int(c_y) - int(y_b)

        print(f"{user_name}, You will be {result1} in {c_y}")
elif Q1 == str(2):
         name = input("Enter Name for who you want to check the Year of Birth: ")
         age = input("Enter Age: ")
         c_y = input("Enter the Current Year: ")

         result2 = int(c_y) - int(age)

         print(f"{name}, Was Born in {result2}")
else:
        print("Invalid input")