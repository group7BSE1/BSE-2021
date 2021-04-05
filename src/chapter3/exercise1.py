time = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))
if time > 40:
    extra_rate = rate * 1.5
    extra_pay = time * extra_rate
    print(f"Pay: {extra_pay}")
else:
    net_pay = time * rate
    print(f"Pay: {net_pay}")