from pydantic import BaseModel,EmailStr,Field,field_validator,model_validator,computed_field
from typing import Optional, Annotated




## TOPICS COVERED 
# -  Field : for annotation
# - field_validator
# -  model_validator : not implemented but easy peasy 
# -  computed_field
# - serialization  : for exportation 


class Student(BaseModel):
    
    name : str 
    rollNo :int = Field(gt=14) 
    pct  :  Optional[int]= None 
    age  :  Optional[int]  =  None
    email : Annotated[EmailStr,Field(max_length=40,title="Email of the student",
        description="write only institution email",examples=["rishu@iit.ac.in","nitiksh@iit.ac.in"])]

    
    
    ## field validator make changes only in one field 
    ## model validator make changes in multiple fields 
    
    @field_validator("name")
    @classmethod
    def transform_name(cls,val):
        ## cls => the main class student if any other method exists then we can directly use that method here 
        ##  val => main value we want to use 
        ## this type of fxns can be used for any transformation and validation 
        return val.upper()
    
    
    @field_validator("age")
    @classmethod
    def validate_age(cls,val):
        
        if 0 < val < 25:
            return val 
        else:
            raise ValueError
        
    @computed_field
    @property
    def validate_pct(self) -> bool:
        if self.pct >  95 :
            eligible_scholarship =  True
        else:
            eligible_scholarship = False 
        
        return eligible_scholarship
    
    
    

obj = {"name":"rishabh","pct":97,"age":6,"rollNo":151,"email":"rishu@gmail.com"}
s1 =  Student(**obj)

## serialization 
print(s1.model_dump())
print(s1.model_dump(include=["name","pct"]))
print(s1.model_dump(exclude_unset=True)) # values that are not passed while not get exported 