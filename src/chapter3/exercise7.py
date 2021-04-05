location = input("Enter name of city: ")
pay = input("Enter salary: ")

try:
    location = location.lower()
    payment = int(pay)

    if(location == "space"):
        decision = "Without a doubt, I’ll take it"
    elif(location == "mbarara"):
        if(payment <= 4000000):
            decision = "No Thanks, I can find something better"
        else:
            decision = "Sure, I can work with this"
    elif(location == "kampala"):
        if(payment < 10000000):
            decision = "No way!"
        else:
            decision = "Sure, I can work with this"
    elif(payment >= 6000000):
        decision = "Sure, I can work with this"
    else:
        decision = "No Thanks, I can find something better"

    print(f"Decision: {decision}")
except:
    print("Error, failed to execute")