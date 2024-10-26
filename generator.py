# def num():
#     print("returning 1st number")
#     return 10
#     return 20
#     return 30



# print(num())
# print(num())
# print(num())


# ot:
# returning 1st number
# 10
# returning 1st number
# 10
# returning 1st number
# 10




# def num():
#     print("yieldin 1st number..")
#     yield 10
#     print("yieldin 2st number..")
#     yield 20
#     print("yieldin 3st number..")
#     yield 30


# n1=num()
# print(n1.__next__())
# print(n1.__next__())
# print(n1.__next__())                                           example

# yieldin 1st number..
# 10
# yieldin 2st number..
# 20
# yieldin 3st number..
# 30





def usn_generator(college,yera,stream):
    num=1
    while True:
        yield college + str(yera) + stream + str(num)
        num+=1



s=usn_generator(yera=2022,stream="cs",college="BJC")

for i in range(1,100):
    print(s.__next__())




# while True:
#     try:
#         print(s.__next__())

#     except:
#         print("")




