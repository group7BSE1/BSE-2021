def computegrade():
    inp = input("Enter score: ")
    try:
        score = float(inp)
        if score >1.0:
            print("Bad score")
        elif score >=0.9:
            print("A")
        elif score >= 0.8:
            print("B")
        elif score >=0.7:
            print("C")
        elif score >=0.6:
            print("D")
        elif score <0.6:
            print("F")

    except ValueError:
        print("Bad score")


computegrade()