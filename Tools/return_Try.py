from returns.result import Success , Failure 


def even_number(a :  int):
    
    if isinstance(a,int):
        if a % 2 == 0 :
            return Success("Even number")
    
    return Failure("not even number")



while True :
     number = input()
     
     if number in ["q","quit","exit"]:
         break 
     
     ans = even_number(int(number))
     if isinstance(ans,Success):
         print("case successful")
     