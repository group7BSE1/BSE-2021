num = 0
total = 0
while True:
	number = input("Enter a number: ")
	if number == "done":
	    break
	try:
	    numb = float(number)
	except:
	    print("invalid input")
	    continue
	num = num + 1
	total = total + numb

print(int(total), num, total/num)
