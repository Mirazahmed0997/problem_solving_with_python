with open('sample_file.txt',"w+") as file:
    file.write("Hello World")
    file.seek(0)
    print(file.read())
    

    file.truncate(5)
    file.seek(0)
    print(file.read())