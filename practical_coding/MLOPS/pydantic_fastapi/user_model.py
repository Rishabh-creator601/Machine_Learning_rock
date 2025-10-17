from pydantic import BaseModel,EmailStr,Field,computed_field
from typing import List,Optional




class User(BaseModel):
    
    
    id : str 
    name : str 
    email : EmailStr 
    age : int  = Field(gt = 12)
    skills : List[str]
    
    
    @computed_field
    @property
    def n_skills(self) -> int:
        return len(self.skills)
    
    

class User_Update(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(default=None, gt=12)
    skills: Optional[List[str]] = None

    @computed_field
    @property
    def n_skills(self) -> int:
        # Handle None case safely
        return len(self.skills or [])

    
    
    
# obj =  {"id":"U004","name":"rishabh","email":"rishabhagarwal@gmail.com","age":18,"skills":["python","java","cpp","react"]}
# u1 =  User(**obj)

# print(u1)