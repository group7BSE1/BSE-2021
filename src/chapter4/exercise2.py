import math
def investment():
    C = float(input("Initial amount of an investment: "))
    r = float(input("Yearly rate of interest: "))
    t = float(input("Years until maturation: "))
    n = float(input("Times the interest is compounded per year: "))
    p = C*(1 + r/n)**(t * n)
    p = round(p, 2)
    print(f"Final value of the investment: {p}")


investment()