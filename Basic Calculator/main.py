print("Vishy's Basic Calculator\n\n")

print("What you mathematical operator do you want to use")
Q1 = input("1: Multiplication\n2: Division\n3: Addition\n4: Subtraction\nAnswer: ")

if Q1 == "1":
    print("\nHow many numbers you want to Multiply? ")
    Q1_x = input("2, 3 or 4: ")
    
    if Q1_x == "2":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")

        result = int(Q2_1) * int(Q2_2)

        print(f"Your Answer is: {result}")
    
    elif Q1_x == "3":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")

        result = int(Q2_1) * int(Q2_2) * int(Q2_3)

        print(f"Your Answer is: {result}")

    elif Q1_x == "4":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")
        Q2_4 = input("Value 4: ")

        result = int(Q2_1) * int(Q2_2) * int(Q2_3) * int(Q2_4)

        print(f"Your Answer is: {result}")

    else:
        print("Invalid Input")
    
elif Q1 == "2":
    print("\nHow many numbers you want to Divide? ")
    Q1_x = input("2, 3 or 4: ")
    
    if Q1_x == "2":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")

        result = int(Q2_1) / int(Q2_2)

        print(f"Your Answer is: {result}")
    
    elif Q1_x == "3":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")

        result = int(Q2_1) / int(Q2_2) / int(Q2_3)

        print(f"Your Answer is: {result}")

    elif Q1_x == "4":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")
        Q2_4 = input("Value 4: ")

        result = int(Q2_1) / int(Q2_2) / int(Q2_3) / int(Q2_4)

        print(f"Your Answer is: {result}")

    else:
        print("Invalid Input")

elif Q1 == "3":
    print("\nHow many numbers you want to Add? ")
    Q1_x = input("2, 3 or 4: ")
    
    if Q1_x == "2":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")

        result = int(Q2_1) + int(Q2_2)

        print(f"Your Answer is: {result}")
    
    elif Q1_x == "3":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")

        result = int(Q2_1) + int(Q2_2) + int(Q2_3)

        print(f"Your Answer is: {result}")

    elif Q1_x == "4":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")
        Q2_4 = input("Value 4: ")

        result = int(Q2_1) + int(Q2_2) + int(Q2_3) + int(Q2_4)

        print(f"Your Answer is: {result}")

    else:
        print("Invalid Input")

elif Q1 == "4":
    print("\nHow many numbers you want to Subtract? ")
    Q1_x = input("2, 3 or 4: ")
    
    if Q1_x == "2":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")

        result = int(Q2_1) - int(Q2_2)

        print(f"Your Answer is: {result}")
    
    elif Q1_x == "3":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")

        result = int(Q2_1) - int(Q2_2) - int(Q2_3)

        print(f"Your Answer is: {result}")

    elif Q1_x == "4":
        Q2_1 = input("Value 1: ")
        Q2_2 = input("Value 2: ")
        Q2_3 = input("Value 3: ")
        Q2_4 = input("Value 4: ")

        result = int(Q2_1) - int(Q2_2) - int(Q2_3) - int(Q2_4)

        print(f"Your Answer is: {result}")

    else:
        print("Invalid Input")

else:
    print("Invalid Input")