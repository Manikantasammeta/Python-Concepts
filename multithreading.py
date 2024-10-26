import _thread
import time
import threading


# def m1(n):
#     time.sleep(0.5)
#     print("this is m1",n)

# def m2(n):
#     time.sleep(0.5)
    
#     print("this is m2",n)
            



# r=time.time()
# _thread.start_new_thread(m1,("m1",))
# _thread.start_new_thread(m2,("m2",))
# print("time taken to excute two functions is ",time.time()-r)


    
    
# def m1(n=100):
#     print("the sqare number is",n)
#     for i in range(n):
#         time.sleep(0.2)
#         print("sqare is",i*i)
        
        
# def m2(n=100):
#     print("the cube number is",n)
#     for i in range(n):
#         # time.sleep(0.2)
#         print("cube is",i*i*i)
# r=time.time()
# l=[5]

# t1=threading.Thread(target=m1)
# t2=threading.Thread(target=m2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("the time taken for the two functionsis",time.time()-r)


def hi():
    for i in range(100):
        time.sleep(0.1)
        print("hii")
def hello():
    for i in range(100):
        time.sleep(0.1)
        print("hello")
        
print("hiiiiiiiiiii")       
t1 = threading.Thread(target=hi)
t2= threading.Thread(target=hello)
t1.start()
t2.start()
t2.join()
print("hllllllll0")