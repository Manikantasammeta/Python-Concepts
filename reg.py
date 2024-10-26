#                            rg expresion
# 
# import re
# msg=" i am mani and i am from Bapatla"

# e=re.search(1,("am"),msg)
# if e!=None:
#     print("found")
# else:
#     print("not found") 


#                                                          searching for multiple patterens                                            
# 
# import re
# msg=" i am mani and i am from bapatla i am completed my bsc with 83% "
# patteren=["mani","bsc","reddy"]
# for i in patteren:
#     print("searchg",i)
#     if re.search(i,msg):
#         print("match found")
#     else: print("not found")



 
# import re
# email="mani@email.com"                             re.split()
# rt=re.split("e",email)
# print(rt)


# import re
# msg="the most vilonet man once called a man most vaiolent"               # re.findall()
# tt=re.findall("manm",msg)
# print(tt)



 
# import re
# data="JamesBond007"
# # res=re.search('Jam',data)
# # res=re.search("Bond",data)                                      searching the chaacter
# # res=re.search("Jam[a-z][A-Z]",data)
# res=re.search("[A-z][a-z]m[0-9]Bond",data)
# if res !=None:
#     print("matched")
# else:
#     print("matched is not found")


# import re
# data="manikantaressdysammeta"
# res=re.search(". .ni[a-z]",data)
# if res!=None:                                                                searchin next character
#     print("matched found" ,res.span())
#     print(res)
# else:
#     print("not found")

# import re

# email="mani@gmail.com"
# rs=re.search("[a-zA-Z]+@[a-zA-z]+\.com",email)
# if rs!=None:                                                                  searchin patteren
#     print("Matched")
# else:
#     print("not matched")
# print(rs)


# import re

# email="manikanta_999@spiders.in"
# rs=re.search("[a-zA-Z0-9._]+@[a-zA-z]+\.(com|in)",email)
# if rs!=None:
#     #                                                             for every email we have to write all patterens..
#     print("Matched")
# else:
#     print("not matched")
# print(rs)



# import re
# str="mani....inam.....mann........maaa..........maam"
# def check(str,test):
#     for i in str:
#         print(re.findall(i,str))

# str="this is a string @and this is a numbers 1234 and specal characheres # and hast tage & Dont know remove it"

# test=['[a-z+]']
# check(str,test)

# import re

# m=re.findall("mani","mani.txt")
# print(m)

# import re
# msg="man@ika@nta@manik@anta"               # re.split()
# tt=re.split("@",msg,2)
# print(tt)



# import re 
# ms="manikanata reddy and i am from bapatla"
# x=re.sub("a","e",ms,1)
# print(x)




import re 
st="This ia s string@ and it has similarry"
f=re.findall("\d",st)                      #if we dont konw the patteren
print(f)

# o/t:['This ', 'ia ', 's ', 'string@', ' ', 'and ', 'it ', 'has ', 'similarry'] 