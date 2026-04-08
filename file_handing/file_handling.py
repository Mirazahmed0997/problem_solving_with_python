# file= open("sample.txt","r")

#     content = file.readlines()

#     print(content)
#     print(type(content))

#     file.close()

    # print(file.closed)

# -------------------------------------


with open("sample.txt") as file:
    content = file.readlines()

    content = list(map(str.strip,content)) 
    filter_content= filter(lambda x: len(x)>=1,content)

    print(list(filter_content))
    # print(type(content))


    # print(file.closed)

# --------------------------------------

with open("sample.txt") as file:
    for line in file:
       l= line.strip() # to minimise the extra new line
    #    print(l)