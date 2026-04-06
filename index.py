def check(age):

    """
     Check the person is under age or not
    """


    if age < 18:
        print(f'{age} is Under Age')
    else:
        print(f'{age} is Adult')


age= int(input("Enter your age : "))
check(age)

# help(check)


def set(*args):
    for i in args:
        print(i)


set(12,32,43)


def set(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")


set(a=12,b=32,c=43,n_estimator=5)