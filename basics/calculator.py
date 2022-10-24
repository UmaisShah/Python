# simple python calculator using if else
num1=int(input('First number is: '))
num2=int(input('Second number is: '))
op=(input("Insert the operation + or - or / or *"))

if op =='+':
    print(num1+num2)

elif op =='-':
    print(num1-num2)

elif op =='*':
    print(num1*num2)

elif op =='/':
    print(num1/num2)
else:
    print('invalid functionality')