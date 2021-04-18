def computepay():
    try:
        time = int(input("Enter Hours: "))
        rate = int(input("Enter Rate: "))
        if time > 40:
            over = (time - 40) * rate * 1.5
            pay = (40 * rate) + over
            print(f"Pay: {pay}")
        else:
            net_pay = time * rate
            print(f"Pay: {net_pay}")
    except ValueError:
        print("Error, please enter numeric input")


computepay()
