C = "initial amount"
r = "yearly interest rate"
t = "number of years until maturation"
n = "number of times the interest is compounded per year"
p = 'Compound interest'
C = int(input("Enter the initial amount: "))
r = float(input("Enter the yearly interest rate: "))
t = int(input("Enter the number of years until maturation: "))
n = int(input("Enter the number of times the interest is compounded per year: "))
p = C*((1+r/n)**n*t)
print(p)