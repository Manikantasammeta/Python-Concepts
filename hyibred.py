class device:
    def __init__(self,type):
        self.type=type
        #print(self.type)
    def enable(self):
        print("device is enabled")
    def disabled(self):
        print("device id disabled") 
    def update(self):
        print("device updating") 


class audio_device(device):
    def __init__(self,name):
        super().__init__(self)
        self.name=name

    def turn_on(self):
        print("device is on")

    def turn_off(self):
        print("device is off")

class microphon(audio_device):
    def __init__(self,name1,type):
        super().__init__(self)
        self.name1=name1
        self.type=type

    def start_record():
        print("starting recording")

    def stop_recird():
        print("stop recording")

class speker(audio_device):
    def __init__(self,name2,type1):
        super().__init__(self)
        self.name2=name2
        self.type1=type1
        self.volume=10
        print(self.name2)
        print(self.volume)
    def play(self):
        print("palying")

    def current_volume(self):
        print("current volume to-->",self.volume)

    def increase_volume(self):
        entervol=int(input("enter the volume  :"))
        self.volume += entervol
        print("increased volume is -->",entervol)

    def decresing_volume(self):
        entervol1=int(input("enter the volume  :"))
        self.volume-=entervol1
        print("decreasinf volume to -->",self.volume)
    


v1=speker("mani","mpr")
v1.current_volume()
v1.increase_volume()
v1.current_volume()
v1.decresing_volume()
