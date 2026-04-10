

with open("notes.txt","r") as file :
    
    file=file.readlines()

    lines= list(map(lambda x: x.split(','),file))

    line = lines[0]
    length= len(line)

    for i in range(length):
        print(f"{i} {line[i]}")


