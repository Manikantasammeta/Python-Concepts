import mysql.connector as mc
print("ENTER 1 FOR LIST OF DATABASES")
print("ENTER 2 TO KNOW THE CURRENT DATABASE")
print("ENTER 3 FOR LIST OF TABLES")
print("ENTER 4 TO CREATE TABLE")



n=int(input("enter a number: "))

try:
    if n==1:
        con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
        cur=con_obj.cursor()
        cur.execute("show databases;")
        r=cur.fetchall()
        print()
        print("THE DATA BASES ARE",len(r))
        for i in range(1,len(r)+1):
            print(i,r[i][0])
            
            
    if n==2:
        con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
        cur=con_obj.cursor()
        cur.execute("select database();")
        r=cur.fetchall()
        print(r[0][0])
        
        
    if n==3:
        con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
        cur=con_obj.cursor()
        cur.execute("show tables;")
        r=cur.fetchall()
        print()
        print("THE TABLES ARE",len(r))
        for i in range(len(r)+1):
            print(r[i][0])
            
            
    if n==4:
        TABLE_NAME=str(input("ENTER TABLE NAME :"))
        
        con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
        cur=con_obj.cursor()
        cur.execute("show tables;")
        r=cur.fetchall()
        LIST_OF_TAB=[]
        for i in range(len(r)):
            LIST_OF_TAB.append(r[i][0])
        print(TABLE_NAME)
        print(LIST_OF_TAB)
            
        if TABLE_NAME not in LIST_OF_TAB:
            COLUMNS=int(input("enter no of columns :"))
            t=()
            for i in range(1,COLUMNS+1):
                name=input(f"enter the  {i} column name in STR format :")
                data_type=input(f"enter {i} the data type :")
                con=input(f"enter the {i} constrain :")

                t=t+(name,data_type,con)
    
            con_obj=mc.connect(host="localhost",user="root",password="1234",database="mydb")
            cur=con_obj.cursor()
            cur.execute("CREATE TABLE {TABLE_NAME} {t}")
            print("TABLE IS CREATED")
        else:
            print("THE GIVEN TABLE NAME IS ALRADY EXISTING PLZ TRY ANTOTHER NAME")      
                
            
        
        
except:
    print("not connected")


# import mysql.connector as mc
# try:
#     con_obj=mc.connect(host="localhost",user="root",password="1234")
#     cur=con_obj.cursor()
#     cu="insert into student.stu(id,name,branch,ph)values "
#     values=[(3,"reddy","bcom",112345678),(4,"riderddy","bca",987654321),(5,"rowdy","bsc",995955423)]
#     cur.executemany(cu,values)
#     con_obj.commit()
#     print("inserted")
# except:
#     print("not inserted")



# import mysql.connector as mc
# try:
#     con_obj=mc.connect(host="localhost",user="root",password="1234")
#     cur=con_obj.cursor()
#     cur.execute("select * from student.stu")
#     for i in cur:
#         print(*i)
# except:
#     print("not inserted")



# import mysql.connector as mc
# try:
#     con_obj=mc.connect(host="localhost",user="root",password="1234")
#     cur=con_obj.cursor()
#     cur.execute(" student.stu set ph=1111111111 where id=1")
#     con_obj.commit()
#     print("updated")
# except:
#     print("not updated")

