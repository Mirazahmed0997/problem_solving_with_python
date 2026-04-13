
class Mobile:
    def __init__(self,name,model,imei):
        self.__name=name
        self.__model=model
        self.__imei=imei #private attribute
    def charging(self):
        print("Phone is charging") 

    def name_data(self):
        return self.__name
    def model_data(self):
        return self.__model
    def imei_data(self):
        return self.__imei


    def name_setter(self,name): # access to chnage the name only
        self.__name=name    

Iphone= Mobile("Iphone","X pluse","1xkaf1")  

Iphone.charging()

print(Iphone.name_data())
Iphone.name_setter("Ipad")



print(Iphone.name_data())
print(Iphone.model_data())
print(Iphone.imei_data())

