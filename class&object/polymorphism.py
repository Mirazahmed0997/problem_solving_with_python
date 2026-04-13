
class Camera:
    def __init__(self,name):
        self.name=name
    def capture(self):
        print(" A photo is captured")

class Smartphone(Camera):
    def __init__(self,name,resulation):
        super().__init__(name)
        self.resulation=resulation
    def capture(self):
        print("captured by phone")    
            
class Dslr(Camera):
    def __init__(self,name,resulation):
        super().__init__(name)
        self.resulation=resulation  
    def capture(self):
        print("captured by Dslr")    

class Drone(Camera):
    def __init__(self,name,resulation):
        super().__init__(name)
        self.resulation=resulation  
    def capture(self):
        print("captured by Drone")              

phone= Smartphone("Iphone 8",30)
dslr= Dslr("Cannon 30",70)
drone= Drone("Xbr 1390",40)


phone.capture()
dslr.capture()
drone.capture()