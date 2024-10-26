name=input("Enter your name :")
Lists='''srice 20/kg suger 30/kg salt 5/kg oil 150/kg'''
#decleration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates
items={'rice':20,
       'suger':30,
       'salt':5,
       'oil' :150,}
option=int(input("for list of items enter ::1::"))
if option==1:
    print(Lists)
    for i in range(len(items)):
        inp1=int(input("if u want to buy the items press 1  or 2 to exit :"))
        if inp1==2:
            break
        if inp1==1:
            item=input("Enter your iteams :")
            quantity=int(input("Enter your quantity :"))
            if item in items.keys():
                    price=quantity*(items[item])
                    pricelist.append((item,quantity,items,price))
                    totalprice+=price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                    gst=(totalprice*5)/100
else:
    print("you entered iteam is not avalibul")
inp=input("can i bell the iteams enter ::yes:: :")
if inp=="yes":
    pass
if finalprice!=0:
    for i in range(len(pricelist)):
        print(i,ilist[i],qlist[i],plist[i])
