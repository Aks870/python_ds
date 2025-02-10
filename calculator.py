a=float(input('enter the first number : '))
b=float(input("enter the second number : "))
print("ADD","SUB","MUL","DIV","EXP","REM","QUE", sep='\n')
c=input("select your operation")
if c=="ADD":
    print(a+b)
elif c=="SUB":
    print(a-b)
elif c=="MUL":
    print(a*b)
elif c=="DIV":
    print(a/b)
elif c=="EXP":
    print(a**b)
elif c=="REM":
    print(a%b)
elif c=="QUO":
    print(a//b)
else:
    print("invalid operator selection: ")
    
      