count = 0
total = 0

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("file can not be opened: ", fname)
    quit()
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        col_pos = line.find(':')
        num = line[col_pos + 1:].strip()
        spam_c = float(num)
        total = total + spam_c

average = total / count
average = round(average, 12)
print('Average spam confidence: ', average)