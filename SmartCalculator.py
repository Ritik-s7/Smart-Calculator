import math as m
import webbrowser
import time

def LCM(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while (True):
        if ((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater + 1
    return lcm

def Factorial(n):
    if n!=0:
        ans = n
        while(n>1):
           ans = ans*(n-1)
           n = n-1
        return ans
    else:
        return 1

def GCD(x, y):
    if y == 0:
        return x
    else:
        return GCD(b, x % y)


print("Hey, I am a smart Calculator. I know operations on only two numbers (Maximum), I'm still learning")
while (True):
    s = input("Enter any mathematical command you want to perform...\n")

    s = s.lower()

    if "your name" in s or "who are you" in s:
        print("Hey, I am Calci")

    # Trigonometric

    elif 'sin' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"Sin({num}) is {m.sin(num2)}")

    elif 'cos' in s or 'cosine' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"Cos({num}) is {m.cos(num2)}")

    elif 'tan' in s or 'tangent' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"The value of Tan({num}) is {m.tan(num2)}")

    elif 'sec' in s or 'secant' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"Sec({num}) is {1 / m.cos(num2)}")

    elif 'Cosec' in s or 'cosecant' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"Cosec({num}) is {1 / m.sin(num2)}")

    elif 'cot' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        num2 = num * 0.0174533
        print(f"Cot({num}) is {1 / m.tan(num2)}")


    elif 'lcm' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f"The LCM of {a} and {b} is {LCM(a, b)}")

    elif 'gcd' in s or 'hcf' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f"The HCF of {a} and {b} is {GCD(a, b)}")

    elif 'factorial' in s or '!' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"{num}! is equals to {Factorial(num)}.")

    elif 'log' in s and 'base' not in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"Log({num}) at base 10 is equals to {m.log10(num)}.")

    elif 'log' in s and 'base' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num1 = int(number[0])
        num2 = int(number[1])
        print(f"Log({num1}) at base {num2} is equals to {m.log(num1,num2)}")


    elif 'cuberoot' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"The Cuberoot of {num} is {m.pow(num, 1 / 3)}")

    elif 'squareroot' in s or 'root' in s or 'sqrt' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"The Squareroot of {num} is {m.sqrt(num)}")

    elif 'square' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"The Square of {num} is {num * num}")

    elif 'cube' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        num = int(number[0])
        print(f"The cube of {num} is {num ** 3}")

    elif 'power' in s:
        number = []
        for integer in s.split():
            if integer.isdecimal() or integer.isnumeric():
                number.append(integer)
        a = float(number[0])
        b = float(number[1])

        print(f"{a} raised to the power {b} is {a ** b}")


    elif 'subtract' in s or 'minus' in s or '-' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f" {a} minus {b} is {a - b}")


    elif 'divide' in s or 'division' in s or '/' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f" {a} Divided by {b} is {a / b}")

    elif 'multiply' in s or 'times' in s or 'into' in s or 'product' in s or 'x' in s or 'X' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f"The Multiplication of {a} and {b} is {a * b}")


    elif 'add' in s or 'plus' in s or 'addition' in s or '+' in s or 'sum' in s:
        number = []
        for integer in s.split():
            if integer.isdigit():
                number.append(integer)
        a = int(number[0])
        b = int(number[1])
        print(f"The Addition of {a} and {b} is {a + b}")

    elif ('youtube' in s or 'ytb' in s) and 'play' not in s:
        print("Sure sir, Opening Youtube for you...")
        time.sleep(3)
        webbrowser.open("https://www.youtube.com")

    elif 'play' in s and 'youtube' in s:
        print("Please enter the name again... ")
        name = input()
        print("Searching for " + name + " on Youtube....")
        time.sleep(3)
        webbrowser.open(f"https://www.youtube.com/results?search_query={name}")

    elif 'google' in s or 'browser' in s or 'chrome' in s:
        print("Sure sir, Opening your browser...")
        time.sleep(3)
        webbrowser.open("https://www.google.com")

    else:
        print("I am unable to proceed this command. Please try to ask in a different way.")
