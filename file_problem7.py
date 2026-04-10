with open("text.txt","r") as file :
    file.seek(6)
    print(file.read())