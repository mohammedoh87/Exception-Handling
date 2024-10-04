try:
    num = int(input("Enter a number: "))
    print("You entered number ", num)
except ValueError as ex:
    print("Exception: ", ex)    
