import math
def sin(x,n):
    sine = 0 

    for i in range(n):
        val = ((-1) ** i) * (x ** (2 * i + 1))/math.factorial(2 * i + 1)
        sine += val
    
    return sine

num = int(input("Enter the number of terms in taylor series:"))
angle_degrees = float(input("Enter the angle in degrees:"))
angle_radians = math.radians(angle_degrees)

# Calculate sine using Taylor series
approx_sine = sin(angle_radians,num)

# Calculate the exact sine using math.sin() for comparison
exact_sine = math.sin(angle_radians)

print(f"Approximated sine value using Taylor series: {approx_sine}")
print(f"Exact sine value using math.sin(): {exact_sine}")