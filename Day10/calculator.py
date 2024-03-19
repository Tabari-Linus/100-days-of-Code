from art import logo

#calculator

#add
def add(n1,n2):
    return n1+n2


#subtraction
def subtract(n1, n2):
    return n1-n2


#division
def divide(n1,n2):
    return n1 / n2


#division
def multiply(n1,n2):
    return n1 * n2


operations = {
    "+":add,
    "-":subtract,
    "/":divide,
    "*":multiply
}

def calculator():
    print(logo)
    num1 = float(input("+"))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        if input("Type 'y' to continue calculating with {answer}:").lower() =='y':
            num1 = answer
        else:
            should_continuw = False
            calculator()

calculator()