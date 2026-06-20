try:
    a = int(input("Enter a number: "))
    print(10 / a)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

except Exception as e:
    print("Error:", e)

finally:
    print("Program ended")