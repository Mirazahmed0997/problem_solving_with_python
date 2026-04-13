from abc import ABC, abstractmethod

class Telephone(ABC):
    @abstractmethod
    def make_call(self):
        pass

    @abstractmethod    
    def capture_photo(self):
        pass


class Sphone(Telephone):
    def make_call(self):
        print("Making a call using Android phone")
    def capture_photo(self):
        print("Capturing photo using Android phone")    

class Iphone(Telephone):
    def make_call(self):
        print("Making a call using Iphone")
    def capture_photo(self):
        print("Capturing photo using Iphone")     

ip=Iphone()
ip.make_call()
ip.capture_photo()