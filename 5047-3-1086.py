a = float(input())
b = float(input())
oper = input()
if oper == "mod":
   if b != 0:
       print(a % b)
   else:
       print('Деление на 0!')
elif oper == "pow":
   print(a ** b)
elif oper == "div":
   if b != 0:
       print(a // b)
   else:
       print('Деление на 0!')
elif oper == "+":
   print(a + b)
elif oper == "-":
   print(a - b)
elif oper == "/":
   if b != 0:
       print(a / b)
   else:
       print('Деление на 0!')
elif oper == "*":
   print(a * b)