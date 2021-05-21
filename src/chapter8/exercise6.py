list = []
while True:
    number = 0.0
    input_num = input('Enter a number: ')
    if input_num == 'done':
        break
    try:
        number = float(input_num)
    except:
        print('Invalid input')
        quit()
    list.append(input_num)
if list:
    print('Maximum: ', max(list) or None)
    print('Minimum: ', min(list) or None)