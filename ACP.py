import math
while True:
 def calculate_trigonometric_values():
    angle_degrees = float(input("Enter an angle in degrees: "))
    angle_radians = math.radians(angle_degrees)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)
    tan_value = math.tan(angle_radians)
    print(f"Sine of {angle_degrees} degrees: {sin_value}")
    print(f"Cosine of {angle_degrees} degrees: {cos_value}")
    print(f"Tangent of {angle_degrees} degrees: {tan_value}")


 calculate_trigonometric_values()
