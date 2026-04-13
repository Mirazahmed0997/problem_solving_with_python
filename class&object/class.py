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
            self.batter_percentage-= photo
            print(f"photo captured in {self.model}")


apple= Phone("Iphone 8","3500mh","40pixel")


