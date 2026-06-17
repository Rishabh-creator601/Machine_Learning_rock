import threading , time ,multiprocessing


def square(x):
    
    for i in range(x):
        print(f"Number : {i}  Squared : {i**2}")
        
        
        
        
        

def Cube(x):
    
    for i in range(x):
        print(f"Number : {i}  Cubed  : {i**3}")

        

t1 = threading.Thread(target=square, args=(10,))
t2 =  threading.Thread(target=Cube, args=(10,))


time_1 =   time.time() 
t1.start()
t2.start()



t1.join()
t2.join()



finished_time =  time.time() - time_1

print(finished_time)
