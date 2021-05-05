def main():
    while True:
        code = input("\nEnter customer code: ")
        if code == "r".upper() or code =="c".upper() or code == "i".upper():
            beg_m = input("Enter beginning meter reading: ")
            if int(beg_m) < 0:
                print("Invalid meter reading")
                main()
            end_m = input("Enter ending meter reading: ")
            if int(end_m) < 0:
                print("Invalid meter reading")
                main()
            else:
                continue
            if end_m > beg_m:
                end_m1 = int(end_m)
            else:
                end_m1 = 1000000000 + int(end_m)
    # calculations
            if code == "r":
                gallons = (int(end_m1) - int(beg_m)) / 10
                bill = 5 + (0.0005 * gallons)
                bills = f"${round(bill, 2)}"
            elif code == "c":
                gallons = (int(end_m1) - int(beg_m)) / 10
                gal = gallons - 4000000
                if gallons <= 4000000:
                    bills = f"${format(1000, '.2f')}"
                elif gallons >= 4000000:
                    bill = 1000 + (0.00025 * gal)
                    bills = f"${format(bill, '.2f')}"
            elif code == "i":
                gallons = (int(end_m1) - int(beg_m)) / 10
                gal = gallons - 10000000
                if gallons <= 4000000:
                    bills = f"${format(1000, '.2f')}"
                elif gallons >= 4000000 and gallons <= 10000000:
                    bills = f"${format(2000, '.2f')}"
                elif gallons >= 10000000:
                    bill = 2000 + (0.00025 * gal)
                    bills = f"${format(bill, '.2f')}"
            print("\nCustomer code: ", code)
            print("Beginning meter reading: ", beg_m)
            print("Ending meter reading: ", end_m.lstrip("0"))
            print("Gallons of water used: ", gallons)
            print("Amount billed: ", bills)
        else:
            quit()

main()
