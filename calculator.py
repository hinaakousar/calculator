def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
     if y == 0:
         return "cannot divide by zero"
     return x/y

def calculator():
    print("Simple Calculator")
    print("Operations")
    print("1.Add")
    print("2.Subtract")
    print("3.multiply")
    print("4.Divide")
    
    choice=input("Select operation(1/2/3/4):")

    if choice not in ['1','2','3','4']: 
        print("invalid choice")   
        return
    num1 =float(input("Enter first number:"))
    num2 =float(input("Enter second number:"))

    if choice =='1':
        result=add(num1,num2)
        print("Result:",result)
    elif choice == '2':
         result=subtract(num1,num2)
         print("Result:",result)
    elif choice == '3':
         result=multiply(num1,num2)
         print("Result:",result)
    elif choice == '4':
         result=divide(num1,num2)
         print("Result:",result)
    



calculator()