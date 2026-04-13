try:
    file = open("exception_data.txt","r")
except Exception as e:
    print(e)
else:
    print(file.read())
finally:
    print("GPU is stopped")

