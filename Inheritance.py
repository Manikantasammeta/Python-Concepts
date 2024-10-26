#                super().__init__
# 
class mani:
    def __init__(self):
        self.x=20
        self.y=10
    def mymethod(self):
        print("my method")
class reddy(mani):
    def __init__(self):
        super().__init__()
        self.a=100
        self.b=200
    def mymethod(self):
        print("my method of class reddy")


r=reddy()
print(r.a,r.b)
r.mymethod()
# class red(reddy):
#     def __init__(self):
#         super().__init__
#         self.a=700
#         self.b=900
#     def mymethod(self):
#         print("my method of class red")

# m=red()
# m.mymethod()
# print(m.a,m.b)


# out put :-->
# my method of class red
# 700 900

# def fun():
#     print("i am fun1")
# if __name__=='__main__':
#     print("m1 printing")
# else:
#     print("m1 file printing")



