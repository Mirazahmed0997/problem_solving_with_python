class Phone:
    catagory = "Electronics"
    # constructor
    def __init__(self,model,battery,camera,batter_percentage=100):
        self.model=model
        self.battery=battery
        self.camera=camera
        self.batter_percentage=batter_percentage
    def charge(self,hour):
        self.batter_percentage += hour
    def capture(self,photo):
        if(self.batter_percentage <=10):
            print("Insufficient Charge")
        else:
            self.batter_percentage -= photo
            print(f"{photo} photos captured in {self.model}")


apple= Phone("Iphone 8","3500mh","40pixel")


#single inheritence

class Smartphone(Phone):
    def __init__(self,model,battery,camera,proccessore):
        super().__init__(model,battery,camera)
        self.proccessore=proccessore
    def fast_charging(self,hour):
        print("Fast charging")
        super().charge(hour)
# pro= Smartphone("Realme C85 pro","3500mh","40pixel","SnapDragon")

# Multiple inheritance

class Cooling_mechanism:
    def __init__(self, cooling_method):
        self.cooling_method=cooling_method
    def cooling_on(self):
        print(f"The system is being cool by {self.cooling_method}")

        

class Smartphone_cooling_System(Smartphone,Cooling_mechanism):
    def __init__(self,model,battery,camera,proccessore,cooling_method):
        Smartphone.__init__(self,model,battery,camera,proccessore)
        Cooling_mechanism.__init__(self,cooling_method)

pro_cooling=Smartphone_cooling_System("Realme C85 pro","3500mh","40pixel","SnapDragon","Air Cooling System")    

pro_cooling.capture(50)
pro_cooling.fast_charging(20)
print(pro_cooling.cooling_method)
print(pro_cooling.batter_percentage)