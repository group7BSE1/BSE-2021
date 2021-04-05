people = int(input("Number of guests: "))
if people <= 50:
    print("The weeding will cost $4,000")
elif people <= 100:
    print("The weeding will cost $10,000")
elif people <=200:
    print("The weeding will cost $15,000")
elif people > 200:
    print("The weeding will cost $20,000")
