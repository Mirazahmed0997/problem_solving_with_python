with open("sample.txt","r") as file:
    print(file.tell()) #initial cursor
    print(file.read(5))
    file.seek(0)
    print(file.tell())
    print(file.read(6))






    # print(file.read(5))

    # print(file.tell())

    # print(file.read())


