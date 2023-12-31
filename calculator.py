# CALCULATOR
num1=eval(input('ENTER YOUR 1ST SUM 1:'))
num2=eval(input('ENTER YUR 2ND SUM 2:'))
opr=input('ENTER YOUR OPREATION :')
if opr=='+':
    print(num1+num2)
elif opr=='-':
    print(num1-num2)
elif opr=='*':
    print(num1*num2)
elif opr=='/':
    print(num1/num2)
# else:
#     print('invaled opr')
if opr !='+' and opr !='-'and opr !='*' and opr !='/':
    print('invaled opr')
