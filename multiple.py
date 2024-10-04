try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result is ", result)
except ZeroDivisionError:
    print("Division by zero is an error ")
except SyntaxError:
    print("Comma is missing, pleaase separate the numbers with comma ',' ")
except:
    print("Wrong input")
else:
    print("NO EXCEPTIONS")
finally:
    print("I will execute no matter what")
