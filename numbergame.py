# import random
# maxn=10
# n=random.randint(1,maxn)
# print("WELCOME TO GUESS THE NUMBER GAME!!!")
# print("guess the number from 1 to%d"%maxn)
# guess=None
# while guess!=n:
#     guess=int(input("you try :"))
#     if guess>n:
#         print("too high")
#         if guess<n:
#             print("too low")
#             print("!!!CONGRATULATIONS,YOU WON THE GAME!!!")

# print({x:x**x for x in range(1,11)})



# print([x for x in range(1,11) if x%2==0])

# for i in xrange(1,33):
#     print(i)



# t=input("enter the text :")
# count = 0
# text =t.index()
# for character in t:
#     if character.isupper():
#         count += 1


#                                  PALINDROME
# r=input("enter the name :")

# s=reversed(r)
# if list(r)==list(s):
#     print("it is PALINDROMR")
# else:
#     print("it is not a palindrome")




# n=input("enter the text :")
# if n.isnumeric():
#     print("it is numaric")
# if n.isalpha():
#     print("it is alphabit")
# if n.isalnum():
#     print("it is alnum")


# txt = "banana"

# x = txt.center(8)

# print(x)
# txt = "I love apples, apple are my favorite fruit"

# x = txt.count("apple",14)

# print
# s1={1,2,3,4,5}
# s2={4,5,6,7,8}

# s1.symmetric_difference_update(s2)
# print(s1)
# s2.symmetric_difference_update(s1)
# print(s2)

# s="python html"
# t=s.title()
# print(t)



# l=[1,2,3,4,5,6,7]
# i=l.remove(3)
# print(l)


# s1={1,2,3,4,5}
# s2={3,4,5,6,7}
# print(s1)
# print(s1.difference_update(s2))
# print(s1)

# s="main sachen"
# print(s.title())
# print(s.capitalize())
# print(s.upper())


# s="Manisachen"
# print(s.split("a"))



# d=["sachegn", "isk", "good", "lis" ,"boy"]
# # print(d.index("g"))
# # print(d.partition("is"))
# o="*".join(d)
# print(o)





# d={1:1,2:2,3:3,4:4,5:5}
# print(d.fromkeys(1))

# d={"r":1,"g":2,"t":4,"u":6,"k":6}
# print(d.fromkeys("k"))
# print(d.pop("r"))
# print(d)
# print(d.setdefault("o",6))
# print(d



# s="mani kanta reddy"
# print(s.replace("a","n",2))

# s="mr.mani kanta reddy"
# print(s.casefold())
# print(s)

# def solve(a, b):
#    return b 
# if a == 0: 
# else:solve(b % a, a)
# print(solve(20, 50))

# n=int(input("enter a number :"))
# b=int(input("enter a number :"))
# c=n*b
# print(c)


# numbers = (4, 7, 19, 2, 89, 45, 72, 22)
# sorted_numbers = sorted(numbers)
# even = lambda a: a % 2 == 0
# even_numbers = filter(even, sorted_numbers)
# print(even_numbers)
# print(type(even_numbers)


# l=[1,2,3,4,5]
# print([x&1 for x in l])








class mani:
    _a=10
    _b=20

    def __init__(self):
        self._x=100
        self._y=200


    def _mani(self):
        print("this is from mani function")


    def _reddy(self):
        print("this from redy function")