string = input('Введіть рядок: ')
reversed_string = " "

for i in range(len(string)-1, -1, -1):
    reversed_string += string[i]

if string == reversed_string:
    print('Введений рядок є паліндромом.')
else:
    print('Введений рядок не є паліндромом.')
