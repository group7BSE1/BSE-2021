str = 'X-DSPAM-Confidence:0.8475'
col_pos = str.find(':')
num = str[col_pos + 1:]
fl = float(num)
print(fl)