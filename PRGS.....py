# i=1                    01:print>>1 2 3 4 5 6 7 8 9 10
# while i<11:
#     print(i,end=" ")
#     i+=1


# n=5                                 number partten
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         i=+1
#     print()

# k=int(input("enter the number :"))      SUM OF THE ENTERD NUMBER
# s=0
# while k>0:
#     d=k%10
#     s=s+d
#     k=k//10
# print("the sum of elemts :",s)


#                                           5=5+4+3+2+1 =15 program
# n=int(input("enter the number :"))
# g=0
# for i in range(n+1):
#     g=g+i
# print("the sem of the ",n ,"digits is :",g)


#                                     FACTERES OF "2"&"3"
# n=int(input("enter the number :"))
# for i in range(1,n):
#     if i%2==0 and i%3==0:
#         print(i,end=" ")

#                                                     IN LIST "%OF2"&"%3"
# l=[x for x in range(1,50) if x%2==0 and x%3==0]
# print(l)

#                                  
# 
#                                            #LIST CONVERT INTO DECT




# l1=[1,1,1,2,3,4,3,2,1,2,3,4,3,4,3,4,3,4,4,3,2,1,2,3,2,1,2,3,2,1,2,3,2,1,4,4,4,3,2,1,2]
# d1={}
# for i in l1:
#     r=l1.count(i)
#     d1.update({i:r})
# print(d1)

#                           CONVERT LIST INTO TUPLE
# l=[1,1,2,3,2,1,2,3,1,2,3,4,5,4,5,6,5,6,7,6,7,8,7,8,7,6,5,4,3,2,1,3,4,5]
# s=set()
# for i in l:
#     r=l.count(i)
#     s.add(i)
# print(s)


#                                 PATTEREN PRG
# n=5
# for i in range(n+1):
#     for j in range(i):
#         print("*",end="")
#     print()
#
#                            PATTEREN PRG
# n=5
# for i in range(n+1):
#      for j in range(i,n):
#          print("*",end="")
#      print()

#                                         CONVERTING "1" TUPLE INTO DICT
# t=(1,2,3,4,5,6,7,8,1,2,3,6)
# d={}
# for i in t:
#     r=t.count(i)
#     d.update({i:r})
# print(d)
#                                         CONVERTING "2" TUPLES IN TO "1"DICT
# t1=1,2,3,4
# t2="mani","sai","gopi","raj"
# d=dict(zip(t2,t1))
# print(d)
#                                               "2"lists convert in to dict
# keys=["mani","reddy","mahi"]
# vals=[1,2,3]
# d=dict(zip(keys,vals))
# print(d)

#                                                      "2"DICT IN TO 1
# d1={1:1,2:2,3:3}
# d2={3:3,4:4,5:5}
# d3={**d1,**d2}
# d3=d1.copy()
# d3.update(d2)
# print(d3)

#                                                     SLICEING THE DICT FROM ANOTHER DICT
# d={"name":"mani","age":21,"sal":50000,"city":"beng"}
# d1={}
# keys=["name","sal"]
# for k in keys:
#     d1.update({k:d[k]})
# print(d1)



