"""Calculator:
+ for addition  || - for subtraction || * for multiplication || / for division """

def calc():
    input_1 = int(input("Please enter your first number: "))
    input_2 = int(input("Please enter your second number: "))
    operation = input("What you want to do with entered numbers? Please enter: +, -, * or / : ")
    if operation == '+':
        print("{} + {}  = ".format(input_1, input_2))
        print(input_1 + input_2)
    elif operation == '-':
        print("{} - {}  = ".format(input_1, input_2))
        print(input_1 - input_2)
    elif operation == '*':
        print("{} * {}  =  ".format(input_1, input_2))
        print(input_1 * input_2)
    elif operation == '/':
        print("{} / {}  =  ".format(input_1, input_2))
        print(input_1 / input_2)
    else:
        print("Please enter: '+', '-', '*' or '/' : ")

calc()