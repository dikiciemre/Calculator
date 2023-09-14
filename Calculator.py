#Plus operation
def plus(x, y):
    return x + y



#Minus operation
def minus(x, y):
    return x - y




#multiplication operation
def multiplication(x, y):
    return x * y



#modding operation
def modding(x, y):
    return x % y



#division operation and control coding
def division(x, y):
    if y == 0:
        return "ERROR! Number cannot be divided by zero." # wWen user entry zero(0) for division, programme give us a alert.
    return x / y



#Loop  coding
while True:
    print("----------------------")
    print("1. Plus")
    print("2. Minus")
    print("3. multiplication")
    print("4. division")
    print("5. modding")
    print("6. Exit")

    Select = input("select your choose : ") # value received from user

    if Select == '6': # when user select 6 button programme is stopping
        print("Exiting...")
        break

    if Select not in ('1', '2', '3', '4','5'):
        print("Wrong Entry! PLease select 1, 2, 3, 4 ,5 or 6. Thank You! ")
        continue

    Number1 = float(input("Please enter Number 1: ")) # progaramme wants to two values for operations
    Number2 = float(input("Please enter Number 2: "))


#progaramme check the operations with if-else coding
    if Select == '1':
        print("Result: ", plus(Number1, Number2))
    elif Select == '2':
        print("Result: ", minus(Number1, Number2))
    elif Select == '3':
        print("Result: ", multiplication(Number1, Number2))
    elif Select == '4':
        print("Result: ", division(Number1, Number2))
    elif Select == '5':
        print("Result: ", modding(Number1, Number2))
