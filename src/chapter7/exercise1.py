fhand = open('mbox-short.txt')
for line in fhand:
    text = line.rstrip().upper()
    print(text)