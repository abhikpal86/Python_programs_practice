a = 6
b = 2
try:
    print(a / b)
    c = int(input("Enter any number: "))
    print(c)
except ZeroDivisionError as e:
    print("Wrong value. ",e)
except ValueError as e:
    print("Give a number. ")
except Exception as e:
    print("Wrong entry")
finally:
    print("End")