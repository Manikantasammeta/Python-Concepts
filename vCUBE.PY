# n=int(input("enter no of participitions :"))
# l=[int(input("enter the score of:" )) for i in range(n)]
# l.sort()
# s=set(l)
# print(list(s)[-2])


# n=int(input("enter a number :"))
# s=1
# while n>1:
#     s=s*n
#     n=n-1
# print(s)


# n1=int(input("Enter no of std_of_eng: "))
# E=[int(input("enter roll no of std :")) for i in range(n1)]
# n2=int(input("Enter no of std_of_french: "))
# F=[int(input("enter roll no of std :")) for i in range(n2)]
# s=len(set(E)-(set(F)))
# print(s)

# input:rabcdeefgyYhFkloomnpOeorteeeeet
#ee,loo,Oeo,eeeee
# 



# import random as re
# l=[1,2,3,4,5]
# def shuffle(fun):  
#     def inner(t):
#         s= [re.choice(t) for i in range(len(t))]   #decorater function
#         return s
#     return inner
  
# @shuffle     
# def f1(r):
#     return r
       
# print(f1(l))


# n1=int(input("enter number :"))        
# n2=int(input("enter  number : "))
# n11=[i for i in range(1,n1) if n1%i==0 ]
# n22=[i for i in range(1,n1) if n2%i==0 ] 

# print(n11,n22)


# k=[1,2,3,4,5]
# m=[11,3,2]
# u=k-m
# print(u)


# s={1,2,3,4,5,6,7,8,9}
# s2={10,1,3,11,21,55,6,8}
# s.difference_update(s2)
# print(s2

import mysql.connector as mc
TABLE_NAME=str(input("ENTER TABLE NAME :"))
C=int(input("enter column: "))
t=[]
for i in range(1,C+1):
        name=input(f"enter the  {i} column name in STR format :")
        data_type=input(f"enter {i} the data type :")
        con=input(f"enter the {i} constrain :")
        t.append(f"{name} {data_type} {con}")
columns_str = ", ".join(t)
con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
cur=con_obj.cursor()
cur.execute(f"CREATE TABLE {TABLE_NAME} {columns_str}")




print(t)