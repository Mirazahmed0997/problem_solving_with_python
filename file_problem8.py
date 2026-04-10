def file(file_name):
        try: 
            with open(file_name,'r') as file :
                content=file.read()
        except Exception as e:
            print(e)
        else: print(content)

        finally: 
            print("Operation Completed")       




file('notes1.txt')