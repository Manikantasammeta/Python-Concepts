class mani:
    def mani_reddy(self):
        print("mani is stearted")

    def rider_reddy(self):
        print('rider isgoing')


class rider:
    def mani_reddy(self):
        print("mani is stoped")

    def rider_reddy(self):
        print("rider came")



def reddy(obj):
    obj.mani_reddy()
    obj.rider_reddy()

p=mani()
q=rider()

reddy(p)
