def add(text):
    with open("append.txt","a+") as file:
        new_file=file.write(text + "\n")
        print(new_file)


add("File uploaded")
add("User logged out")
