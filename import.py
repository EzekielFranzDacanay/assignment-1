#equations 1-10
#assignment dacanay
import matplotlib.pyplot as plt
import math

num = [x for x in range(-10, 11)]

unique_functions = {
    1: lambda: [x**2 - 5 for x in num],
    2: lambda: [x**2 + x - 90 for x in num],
    3: lambda: [x**10 - x**8 + x**2 - 9 for x in num],
    4: lambda: [x**4 + x**3 + x**2 + x + 2 for x in num],
    5: lambda: [(x**2 + x + 12) / (2*x+1) for x in num],
    6: lambda: [math.sin(x) / (4*x+1) for x in num],
    7: lambda: [x**3 + 3*x**2 - 10*x + 4 for x in num],
    8: lambda: [math.cos(x) / (6*x+1) for x in num],
    9: lambda: [(x**3 / (3*x)) - 10*x+1 for x in num],
    10: lambda: [(x+3)*(x+4)*(x-5) for x in num]
}

while True:
    number_problem = int(input("Enter a problem number from (1-10): "))
    if number_problem in unique_functions:
        result = unique_functions[number_problem]()
        break
    else:
        print("imput only numbers from 1-10!")

plt.plot(num, result, label=f'Unique Problem {number_problem}')
plt.xlabel('Input Numbers')
plt.ylabel('Result')
plt.legend()
plt.show()