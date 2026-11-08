from enum import Enum 
from returns.result import Success,Failure
from dataclasses import dataclass

@dataclass
class Loan:
    
    CREDIT_SCORE : int  =  350 
    LOAN_APPROVED : bool =  False 
    INSURANCE_ELIGIBLE : bool =  False # only over 650
    
    

def approve_load(client :  Loan):
    
    if client.CREDIT_SCORE >  500 :
        client.LOAN_APPROVED =  True 
        return Success("loan approved")

    client.INSURANCE_ELIGIBLE = client.CREDIT_SCORE >  650
    
    return client 


print(approve_load(Loan(CREDIT_SCORE=100)))

     