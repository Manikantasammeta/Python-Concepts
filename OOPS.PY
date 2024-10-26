#                                                  EXAMPLE  1

# class mob():
#     def __init__(self,name,price,color,model,ram,):
#         self.name=name
#         self.price=price
#         self.color=color
#         self.model=model
#         self.ram=ram
#     def mob_info(self):
#         print(f"name :{self.name}\nprice :{self.price}\ncolor :{self.color}\nmodel :{self.model}\nram   :{self.ram}")
# m1=mob("samsung",75000,"white","r2","8gb")
# m1.mob_info()
# print()
# m2=mob("ASUS",10000,"red","e12","6GB")
# m2.mob_info()
# print()/

#                                             EXAMPLE  2

# class bank():
#     def __init__(self,name,number,ifcode,type,):
#         self.name=name
#         self.num=number
#         self.ifcode=ifcode
#         self.type=type
#     def bnk(self):
#         print(f"name  :{self.name}\nnumber:{self.num}\nifcode :{self.ifcode}\ntype   :{self.type}")
# b1=bank("state bank",123456789012,"sbi001122","SAVEINGS")
# b1.bnk()
# print()
# b=bank("adhra bank",123456789012,"sbi001122","SAVEINGS")
# b.bnk()
# print()



# class bank():
#     bankname="statebank"
#     bankcode="fic112233"
#     branch="palem"
#     def __init__(self,name,acno,amount):
#         self.name=name
#         self.acno=acno
#         self.amount=amount
#     def bank_info(self):
#         print(f"bankname :{self.bankname}\nbankcode :{self.bankcode}\nbranch   :{self.branch}\n")
#         print(f"name :{self.name}\nacno :{self.acno}\namount :{self.amount}\n")
# b1=bank("manikantareddy",11223344554,5000)
# b1.bank_info()

# b2=bank("manikantareddy",11223344554,5000)
# b2.bank_info()

# b3=bank("manikantareddy",11223344554,5000)
# b3.bank_info()

# import numbergame as n


# p=n.mani()

# print(n.mani._a)
# print(n.mani._b)
# print(p._x)
# print(p._y)
# p._mani()
# p._reddy()

# class emp:
#     def __init__(self,name,age,adds):
#         self.__Name=name
#         self.__Age=age
#         self.__Adds=adds

#     def getname(self):
#         return self.__Name

#     def getadds(self):
#         return self.__Adds

#     def getage(self):
#         return self.__Age

#     def setname(self,name):
#         self.Name=name

#     def setage(self,age):
#         self.Age=age
        
#     def setadds(self,adds):
#         self.Adds=adds


# e=emp("mani",21,"sammetavaripalem")
# print(e.getname())
# print(e.getage())
# print(e.getadds())
# print()
# print()
# e.setadds("perali")
# e.setname("reddy")
# e.setage(21)
# print()
# print()
# print(e.getname())
# print(e.getage())
# print(e.getadds())
        



# class sampl1:
#     def __init__(self):
#         print("it is sample class1")
# class sample2(sampl1):
#     def __init__(self):
#         super().__init__()
#         print("it is sample class2")

# s=sampl1()
# m=sample2()


# a=10
# print(id(a))
# print(id(10))
# 20
# print(id(20))
# print(id(_))



