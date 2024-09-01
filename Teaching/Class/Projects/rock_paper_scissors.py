x = int(input('\033[1m\033[96mNum1: '))
print('\033[93mAddition:\t\t+\nSubtraction:\t-\nMultiplication:\t*\nDivision:\t\t/\nExponent:\t\t^')
z = input('\033[1m\033[96mOperator: ')
y = int(input('\033[1m\033[96mNum2: \033[91m'))
if z == '+':
    print(x+y)
if z == '-':
    print(x-y)
if z == '/':
    print(x/y)
if z == '*':
    print(x*y)
if z == '^':
    print(x**y)
