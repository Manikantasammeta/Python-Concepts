class mani:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def reddy(self):
        print(self.name,self.marks)
    @classmethod
    def get_point(cls,name,marks):
        return cls(name,marks*2)





m=mani("io",879)
marks="890"
name="980"
r=mani.get_point("try",768)
m.reddy()