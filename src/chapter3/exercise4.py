age = int(input("What's your age: "))
if age >= 18:
    print("You can vote")
elif age > 0 and age <= 17:
    print("Too young to vote")
elif age < 0:
    print("You are a time traveller")