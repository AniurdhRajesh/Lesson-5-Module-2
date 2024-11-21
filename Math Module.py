import math
while True:
 def simple_math_demo():
     print("Simple Demo of the math Module:\n")
 
     print(f"Value of Pi: {math.pi}")
     number = int(input("Enter a number for Square Root : "))
     print(f"Square root of {number}: {math.sqrt(number)}")
     n = int(input("Enter a number to find factorial : "))
     print(f"Factorial of {n}: {math.factorial(n)}")
     base = int(input("Enter the base for Exponential : "))
     exponent = int(input("Enter the exponent : "))
     print(f"{base}^{exponent}: {math.pow(base, exponent)}")
 
     angle_degrees = int(input("Enter an angle to find sin : "))
     angle_radians = math.radians(angle_degrees)
     print(f"Sine of {angle_degrees} degrees: {math.sin(angle_radians)}")
 
 if __name__ == "__main__":
     simple_math_demo()
