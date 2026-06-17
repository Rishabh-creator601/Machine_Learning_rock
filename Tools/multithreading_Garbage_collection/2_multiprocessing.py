import multiprocessing, time 





def square(x):
    
    for i in range(x):
        print(f"Number : {i}  Squared : {i**2}")
        
        
        
        
        

def Cube(x):
    
    for i in range(x):
        print(f"Number : {i}  Cubed  : {i**3}")




# Everything that actually executes MUST be inside this block
if __name__ == "__main__":

    p1 = multiprocessing.Process(target=square, args=(10,))
    p2 =  multiprocessing.Process(target=Cube, args=(10,))


    time_1 =   time.time() 
    p1.start()
    p2.start()



    p1.join()
    p2.join()



    finished_time =  time.time() - time_1

    print(finished_time)
