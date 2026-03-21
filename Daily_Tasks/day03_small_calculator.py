print ("==============================")
print ("MY PYTHON CALCULATOR")
print ("==============================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

add = num1 + num2
sub = num1 - num2
mul = num1 * num2

if num2 != 0:
    div = num1 / num2

else:
    div = "Error..! (Can't Divide by 0)"

print(f"\n--- Results for {num1} and {num2} ---")
print(f"\n5Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div:.2f}")

input("\nPress Enter to exit...")
