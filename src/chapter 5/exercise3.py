print("Welcome to the vending machine change maker programme")
print("Change maker initialized.")
print("Stock contains:")
print("     25 nickels")
print("     25 dimes")
print("     25 quarters")
print("     0 ones")
print("     0 fives")
while True:
    price = input("\nEnter the purchase price (xx.xx) or 'q' to quit: ")
    if price == "q":
        quit()
    else:
        price = float(price)
        amount = int(round(price * 100))
        div = amount % 5
        if div == 0 and price > 0:
            print("\nMenu for deposits:")
            print("   'n' - deposit a nickel")
            print("   'd' - deposit a dime")
            print("   'q' - deposit a quarter")
            print("   'o' - deposit a one dollar bill")
            print("   'f' - deposit a five dollar bill")
            print("   'c' - cancel the purchase")
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents")