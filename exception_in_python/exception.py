n = int(input())

try:
    a= 10/n
except ZeroDivisionError:
    print("You Cant Divide a Number with 0")
    a=None

print(a)
print('Hello World')



try:
    x=y
except Exception as e: #handle any error using Exception class
    print("Y is not defined")
    x=None

print(x)