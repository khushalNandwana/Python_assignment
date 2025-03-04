print("Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
choice=input("enter the user's choice(1/2/3/4)")
a=int(input("enter the a's value"))
b=int(input("enter the b's value"))
if choice=='1':
    output=a+b
    print("additon of two number is",output)
elif choice=='2':
    output=a-b
    print("subtraction of two number is",output)
elif choice=='3':
    output=a*b
    print("Multiplication of two number is",output)
elif choice=='4':
    if b==0:
        print("error")
    else :
        output=a/b
        print("division of two number is",output)
else:
    print("invalid input please re-enter the number")
