import math

print(" normal calculation, calculus, trigonometry")
select = input("Select one for to use: ")
if select.lower() == "normal calculation":
    def sum_cal():
        sum = num1 + num2
        print(sum)
    
    def minus_cal():
        if num1 > num2:
            minus = num1 - num2
        else: 
            num2 > num1
            minus = num2 - num1
            print(minus)

    def multi_cal():
        mul = num1 * num2
        print(mul)

    def div_cal():
        div = num1 / num2
        reverse = 1/div
        print(div)
        print(reverse)
    
    num1 = eval(input("Please input the number: "))
    num2 = eval(input("Please input the number: "))
    print("Which one you wanna use?")
    print("sum, abstract, multiply, divide")

    choice = input("Choose 1 method ")


    if choice.lower() == "sum":
        command = sum_cal()
    
    elif choice.lower() == "abstract":
        command = minus_cal()
    
    elif choice.lower() == "multiply":
        command = minus_cal()
    
    else: 
        choice.lower() == "divide"
        command = div_cal()
elif select.lower() == "calculus":
    def area_cal():
        radius = eval(input("Input the radius: "))
        area = float(math.pi * radius**2)
        print(f"The area is {area:.2f}")

    def log_cal():
        base = eval(input("Input the Type of base: "))
        number = eval(input("Input the number: "))
        log_result = math.log(number, base)
        print(f"The logarithm of {number} with base {base} is {log_result}")
    
    def exp_cal():
        power = eval(input("Input the number of power: "))
        base = eval(input("Input the base: "))
        exp_result = math.pow(base, power)
        print(exp_result)
            
    print("Area, Limit, Derivative, Integral, Exponential, Logarithm")
    choice1 = input("Choose: ")
    if choice1.lower() == "area":
        command = area_cal()
    elif choice1.lower() == "logarithm":
        command = log_cal()
    elif choice1.lower() == "exponential":
        command = exp_cal()