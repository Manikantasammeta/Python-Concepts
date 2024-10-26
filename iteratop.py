# l=[1,2,3,4]
# print(type(l))
# print(dir(l))
# print()



# l1=l.__iter__()
# print(type(l1))
# print(dir(l1))
# print(l1.__next__())                              converting list to iterator
# print(l1.__next__())
# print(l1.__next__())
# print(l1.__next__())
# print(l1.__next__())
# print(l1.__next__())


# l=[1,2,3,4,5,6,7]

# l1=l.__iter__()

# while True:                               example
#     try:
#         v=l1.__next__()
#         print(v)
#     except:
#         raise StopIteration


# l=[1,2,3,4,5,6,7]

# l1=l.__iter__()

# while True:                               
#     try:
#         v=l1.__next__()
#         print(v)
#     except StopIteration:
#         break


# class num:
#     def __init__(self):
#         self.no=1


#     def __iter__(self):
#         return self
                                        # creating a own itearator object  
#     def __next__(self):
#         while self.no<=10:
#             val=self.no
#             print(val,end=" ")
#             self.no+=1


# n1=num()
# n1.__next__()


