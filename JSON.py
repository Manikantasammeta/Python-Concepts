# import json


# emp='{"name":"mani","id":"32","salary":"9000","job":"sw"}'
#                                                                           loads()

# r=json.loads(emp)
# print(r)



# import json

# emp={"name":"mani","id":"32","salary":9000,"job":"sw"}
#                                                                   dumps()
# d=json.dumps(emp)
# print(type(d))
# print(d)


# import json

# try:
#     r=open("mani.json","r")
#     mani=json.load(r)
#     print(type(mani))                                                load()
#     print(mani)
# except FileNotFoundError as fe:
#     print("reason",fe)



# import json

# emp={"name":"mani","id":"32","salary":"9000","job":"sw"}

# try:
#     h=open("manireddi.json","w")                                      dump()
#     json.dump(emp,h)
#     print("dumped")
# except:
#     print("erroe occured")




# import pickle

# l1=["mani","32","9000","sw"]                      dumps()

# print(type(l1))
# mi=pickle.dumps(l1)
# print(type(mi))
# print(mi)




# #unpickling
# r=pickle.loads(mi)
# print(r)                                            loads()
# print(type(l1))





# import pickle
# emp=["mani","32","9000","sw"] 
# try:
#     r=open("mani.pkl","wb")                                          #pickle
#     mani=pickle.dump(emp,r)
#     print(type(mani))                                               #dump()
#     print(mani)
# except FileNotFoundError as fe:
#     print("reason",fe)




# import pickle
# try:
#     r=open("mani.pkl","rb")                                          #pickle
#     man=pickle.load(r)                                                #load( )
#     print(man)                                               
# except FileNotFoundError as fe:
#     print("reason",fe)




# print(list(filter(lambda n:n%2==0,range(1,51))))
# print(list(map(lambda n:n*n,range(1,11))))


from functools import reduce

print(reduce(lambda a,b:a+b,range(1,5)))