list = []
while True:
    number = 0
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = float(number)
    except:
        print("Invalid input ")
        continue
    list.append(number)

if list:
    print("maximum:", max(list))
    print("minimum:", min(list))
