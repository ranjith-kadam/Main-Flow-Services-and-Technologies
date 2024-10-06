# Basic Arithematic operations

def add(x,y):
    print("Addition of Two Numbers is ",x+y,"\n")

def subtract(x,y):
    print("Substraction  of Two Numbers is ",x-y,"\n")

def multiply(x,y):
    print("Multiplication of Two Numbers is ",x*y,"\n")

def divide(x,y):
    print("Division of Two Numbers is ",x+y,"\n")


print("Arithematic Operations Program \n")
print("*********** MENU *************\n")

while True:
    print("1. Addition ")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division ")
    print("5. exit")

    choice = input("Enter your your choice : ")
    if choice == "5":
        break

    elif choice in ["1", "2", "3", "4"]:
        num1=int(input("Enter First Number: "))
        num2=int(input("Enter Second Number: "))

        if choice =="1":
            add(num1,num2)
        elif choice =="2":
            subtract(num1,num2)
        elif choice =="3":
            multiply(num1,num2)
        elif choice == "4":
            divide(num1,num2)

        else:
            print("\nInvalid choice , Please try again.")
          
