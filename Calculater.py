import os
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def floor(a,b):
    return a//b
def modulo(a,b):
    return a%b
operation_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "//":floor,
    "%":modulo
}
def calculator():
   number1=float(input("Enter first Number :-"))
   for symbol in operation_dict:
       print(symbol)
   continue_flag=True
   while continue_flag:
           
         op_Symbol=input("pick up symbol for operations :-")    
         
         number2=float(input("Enter second number"))
         calculater_function=operation_dict[op_Symbol]
         output=calculater_function(number1,number2)
         print(f"{number1} {op_Symbol} {number2} = {output}")
         should_continue=input(f"Enter 'y' to continue calculation with {output} or'n' to strat a new calculation and 'x' to  Exist :-").lower()
         if should_continue=="y":
             number1=output
         elif should_continue=="n":
             continue_flag==False
             os.system('cls')
             calculator()
           
         elif should_continue=='x':
             continue_flag=False
         else:
             print("Invailed Input")
             print()    
calculator()             
       
   
   