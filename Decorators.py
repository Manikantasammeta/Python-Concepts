# def mydec(fun):
#     def innerfun():
#         print("this is inner fun")
#         fun()
#         print("aftr inner fun")
#     return innerfun


# def myfun():
#     print("this is fun")

# val=mydec(myfun)
# # print(val)
# # print(type(val))
# # val()



# def mydec(fun):
#     def innerfun():
#         print("before fun")
#         fun()
#         print("after fun")
#     return innerfun
#                                      @decorator
# @mydec
# def myfun():
#     print("this is fun")

# myfun()





# def increse(fun):
#     def incea_by_1():
#         print("increaseing by 1..")
#         new_val=fun()+1
#         return new_val
#     return incea_by_1             examplle

# @increse
# def givenum():           
#     return 5
# print(givenum())

# from datetime import datetime


# def lo_intime(fun):
#     def wrapper():
#         print("hello",fun.__name__)
#         fun()
#         print((f"{fun.__name__}  log in time is :{datetime.today().strftime('%y-%m-%d %H:%M:%S')}"))

#     return wrapper

# @lo_intime
# def mani():
#     print("mani log in time")


# @lo_intime
# def reddy():
#     pass


# reddy()

