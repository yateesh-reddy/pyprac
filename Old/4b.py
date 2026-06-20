try:
    a = int(input("Enter number: "))
    b = int(input("Enter divisor: "))
    print(a / b)

except ZeroDivisionError:
    print("Division by zero")

except ValueError:
    print("Invalid input")

except Exception as e:
    print("Error:", e)

finally:
    print("Program Ended")