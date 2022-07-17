n = 0
while n < 1:

    print("bros calculator")
    operation = input('''
            (sub)subtraction
            (add)addition
            (div)division
            (mul)multiplication
            (stop)close the cal: ''')

    if operation.lower() == "stop":
        print("ty for using me")
        break

    x = float(input('the first number: '))
    y = float(input("the second number: "))

    if operation.lower() == "sub":
        print(x - y)
    else:
        if operation.lower() == "add":
            print(x + y)
        else:
            if operation.lower() == "div":
                print(x/y)
            else:
                if operation.lower() == "mul":
                    print(x*y)