# 
#                                               READ()
# fh=None
# try:
#     fh=open("mani.txt","r")
#     msg=fh.read()
#     print(msg) 
# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()


#                                                   position()
# fh=None
# try:
#     fh=open("mani.txt","r")
#     msg=fh.tell()
#     print(msg) 

#     CH=fh.read(3)
#     print(CH)

#     msg=fh.tell()
#     print(msg)

#     CH=fh.read(7)
#     print(CH)
#     msg=fh.tell()
#     print(msg)

# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()




#                                                           Seek()
# fh=None
# try:
#     fh=open("mani.txt","r")
#     t=fh.tell()
#     print(t)
#     fh.seek(4)
#     t=fh.tell()
#     print(t)
#     ch=fh.read(4)
#     print(ch)

# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()


#                                                           readlines()
# 
#  fh=None
# try:
#     fh=open("mani.txt","r")
#     ch=fh.readlines()
#     for i in ch:
#         print(i)
    

# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()



#                                                          append()
# fh=None
# try:
#     fh=open("mani.txt","a")
#     if fh.writable()==True:
#         print("it is opened")
#     fh.write("\nReddy reddt bhbjjnn")
# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()





#                 writting data from one txt to another text
# 
#  fh=None
# th=None
# try:
#     th=open("reddy2.txt","w")
#     fh=open("mani.txt","r")
#     m=fh.readlines()
#     for i in m:
#         th.write(i)
#     print("completed")

# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()




# fh=None
# th=None
# l=["a","e","i","o","u"]
# try:
#     fh=open("mani.txt","r")
#     th=open("reddy2.txt","w")
#     m=fh.  
#     for i in m:
#         if i in l:
#             print(i,end=" ,")

# except FileNotFoundError as fe:
#     print("reason",fe)
# finally:
#     if fh!=None:
#         fh.close()
#     if th!=None:
#         th.close()


fh=None
th=None
l=["a\n","e","i","o","u"]
fh=open("mani.txt","r")
th=open("reddy2.txt","w")
th.write("mnb")  


