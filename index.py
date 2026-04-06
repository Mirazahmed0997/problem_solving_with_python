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

help(check)