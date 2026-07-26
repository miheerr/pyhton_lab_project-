def add(a, b):
    print("Result:", a + b)

def sub(a, b):
    print("Result:", a - b)

def mul(a, b):
    print("Result:", a * b)

def div(a, b):
    if b != 0:
        print("Result:", a / b)
    else:
        print("Division by zero is not allowed!")

def aoc(r):
    print("Area of Circle:", 3.14 * r * r)

def coc(r):
    print("Circumference of Circle:", 2 * 3.14 * r)

def aor(l, b):
    print("Area of Rectangle:", l * b)

def avg(x, y, z):
    print("Average:", (x + y + z) / 3)

def per(x, y, z):
    print("Percentage:", ((x + y + z) / 300) * 100)

def SI(p, r, t):
    print("SI:", ((p*r*t)/100))

def swap(a, b):
    a,b = b,a
    print("After swaping:")
    print("a:", a)
    print("b:", b)

def ctf(c):
    print("F: ", (c*(9/5))+32)

def exp(a, b, c, d):
    print("Expression: ", ((a+b)*c)/d)

def sal(a):
    print("Gross Salary:", a+((a*10)/100)+((a*12)/100)+((a*8)/100))

def pnz(a):
    if a>0:
        print(a," is a positive number.")
    elif a<0:
        print(a," is a negative number.")
    else:
        print("it's a zero oooooooooooooooooooooooooo.")

def odd_even(a):
    if a % 2 == 0:
        print(a, "is an Even number.")
    else:
        print(a, "is an Odd number.")

def vote_eligibility(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote yet.")

def greater_between_two(a, b):
    if a > b:
        print(a, "is greater than", b)
    elif b > a:
        print(b, "is greater than", a)
    else:
        print("Both numbers are equal.")

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")

def greater_between_three(a, b, c):
    if a > b and a > c:
        print(a, "is greater than", b , c)
    elif b > a and b > c:
        print(b, "is greater than", a , c)
    else:
        print(c, "is greater than", a , b)

def bill(unit):
    if unit <= 100:
        print("Total Bill: ", (100 * 3.50) + unit)
    elif unit <= 200:
        print("Total Bill: ", ((100 * 3.50) + (100 * 5)) + unit)
    elif unit <= 300:
        print("Total Bill: ", ((100 * 3.50) + (100 * 5) + (100 * 7)) + unit)

while True:
    print("\n===== MENU =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Area of Circle")
    print("6. Circumference of Circle")
    print("7. Area of Rectangle")
    print("8. Average")
    print("9. Percentage")
    print("10. Simple interest")
    print("11. swaping")
    print("12. Celsius To Fahrenheit")
    print("13. Expression")
    print("14. Gross Salary")
    print("15. Postive ,Negative ,Zero")
    print("16. Odd even")
    print("17. vote eligibility")
    print("18. Greater between two number")
    print("19. leap yaer")
    print("20. Greater between three number")
    print("21. Electricity bill")
    print("0. Exit")
   
    choice = int(input("Enter your preference: "))
   
    if choice == 1:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        add(a, b)
    elif choice == 2:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        sub(a, b)
       
    elif choice == 3:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        mul(a, b)
       
    elif choice == 4:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        div(a, b)
       
    elif choice == 5:
        r = int(input("Enter the radius: "))
        aoc(r)
       
    elif choice == 6:
        r = int(input("Enter the radius: "))
        coc(r)
       
    elif choice == 7:
        l = int(input("Enter the length: "))
        b = int(input("Enter the breadth: "))
        aor(l, b)
       
    elif choice == 8:
        x = int(input("Enter the First number: "))
        y = int(input("Enter the Second number: "))
        z = int(input("Enter the Third number: "))
        avg(x, y, z)
       
    elif choice == 9:
        x = int(input("Enter the First number: "))
        y = int(input("Enter the Second number: "))
        z = int(input("Enter the Third number: "))
        per(x, y, z)
       
    elif choice == 10:
        p = int(input("Enter the Amount: "))
        r = int(input("Enter the Rate: "))
        t = int(input("Enter the Year: "))
        SI(p, r, t)
    elif choice == 11:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        swap(a,b)
    elif choice == 12:
        c = float(input("Enter the value of Celsius: "))
        ctf(c)
    elif choice == 13:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        c = int(input("Enter the Third number: "))
        d = int(input("Enter the Fourth number: "))
        exp(a, b, c, d)
       
    elif choice == 14:
        a = int(input("Enter your salary: "))
        sal(a)
       
    elif choice == 15:
        a = int(input("Enter the number: "))
        pnz(a)
       
    elif choice == 16:
        a = int(input("Enter the number: "))
        odd_even(a)
       
    elif choice == 17:
        age = int(input("Enter your age: "))
        vote_eligibility(age)
       
    elif choice == 18:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        greater_between_two(a, b)
       
    elif choice == 19:
        year = int(input("Enter the year: "))
        leap_year(year)

    elif choice == 20:
        a = int(input("Enter the First number: "))
        b = int(input("Enter the Second number: "))
        c = int(input("Enter the third number: "))        
        greater_between_three(a, b, c)

    elif choice == 21:
        unit = int(input("Enter your unit: "))
        bill(unit)
       
    elif choice == 0:
        print("Thank you! Program terminated.")
        break
    else:
        print("Invalid choice! Please try again.")
       
    again = input("\nDo you want to perform another operation? (y/n): ").lower()
    if again != "y":
        print("Thank you! Goodbye.")
        break