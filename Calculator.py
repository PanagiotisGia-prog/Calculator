#Simple calculator made in python

def add(x, y):
    return x + y
    
def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y
    
def divide(x, y):
    return x / y

operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

def My_Calculator():
    
    calculator = True
    try:
        num1 = float(input("Give a number\n"))
    except ValueError:
        print("Error: Please give a number")
        calculator = False
        
    while calculator:
        try:
            num2 = float(input("Give another number\n"))          
            for o in operators:
                print(o)
            op = input("Please choose one of the operators you see above\n")
            if op in operators:
                if op == "/" and num2 == 0:
                    print("You can't divide by zero")
                    continue
                result = operators[op](num1, num2)
                print(f"{num1} {op} {num2} = {result}")
            else:
                print("Invalid operator. please choose only between +, -, * or /")
            calc = input(f"Do you want to continue with the current {result}. Type (YES/NO)\n")
            if calc == "yes":
                num1 = result
            else:
                calculator = False
                break
        except ValueError:
            print("Error: I asked for a number")

def repeat():
    while True:
        My_Calculator()
        user = input("Wanna make another calculation or turn off the calculator? Typer (New/Off) \n").lower()
        if user != "new":
            print("Thank you for using my calculator!")
            break

repeat()
