def power(base,exponent=None):
    if exponent is None:
        print(base * base) 
    else: 
            result=1
            for i in range(exponent):
                result =result * base
                print(result)
  


# def power(base, exponent=None):
#     if exponent is None:
#         print(base * base)
#     else:
#         result = 1
#         for i in range(exponent):
#             result *= base
#         print(result)

power(4,4)
