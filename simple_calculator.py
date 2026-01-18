try:
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))

    print("what kind of operation you want to perform")
    o=input("enter the expression")
    match o:
        case "+":
            print(f"the result is{a+b}")
        case "/":
            print(f"the result is{a/b}")
        case "*":
            print(f"the result is{a*b}")
        case "-":
            print(f"the result is{a-b}")

except Exception as e:
    print("enter the valid input")


