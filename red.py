#                                                    HOW WE TAKE INPUT IN DICT
# # stu ={}
# # b= int(input("enter a element:::::"))
# # for i in range(0,b):
# #     key=input("enter key::")
# #     value=int(input("enter value::"))
# #     stu[key]=value
# # print(stu)

# #                                                   HOW WE TAKE INPUT IN SETS
# # d = set()
# # b= int(input("enter a element:::::"))
# # for i in range(0,b):
# #     key=input("enter key::")
# #     d.add(key)
# # print(d)

     # #                                             HOW WE TAKE INPUT IN LIST
# lst1 = []
# b= int(input("enter a element:::::"))
# for i in range(0,b):
#     ele = int(input("enter element"))
#     lst1.append(ele)
# print(lst1)
# lst1.extend(8)
# print(lst1)

# class myclass:
#      x=90
#      y=80
#      def __init__(self):
#           self.s=20
#           self.u=30


# m=myclass()
# print(m.s)



# n=(-9,-54,1,2,3,4,5,6,7,8,9)
# b=0
# for i in n:
#      if i<=n[0]:
#           b=i
# print(b)



# n=int(input("n:"))
# b=[]
# m=str(n)
# for i in m:
#      if i in b:
#           pass
#      else:
#           b.append(i)
#      b.sort()
# print(*b)


# b=[1,2,3,3,3,4,4,5,1,2,3,4,5,6,]
# d=[]
# for i in b:
#      if i in d:
#           pass
#      else:
#           d.append(i)
#      b.sort()
# print(d)

# n=[]
# n1=[1,2]
# n3=[1,2,3]
# s=[n,n1,n3]
# for i in s:
#      if not i:
#           print(i," is empty")


# n=["mani","reddy","sai","rowdy reddy"]
# f=[]
# for i in n:
#      r=len(i)
#      if r<len(n[0]):
#           f.append(i)
# print(f)

# s="manikanta reddy manikanta reddy manikanta rdeddy"
# l=[]
# for i in s:
#      if i not in l:
#           print(i,":",s.count(i),end="  ,")
#           l.append(i)
#      else:
#         pass


# def mani(n,i=1,):
#      if n>1:
#           return mani(n-1,i*n)
#      return i

# o=mani(int(input("n:")))
# print(o)

# def mani(n):
#      if n==1:
#           return n
#      else:
#           return n*mani(n-1)
# print(mani(5))

# class reddy:
#     def clas(self):
#         print("i am reddy")

import cv2