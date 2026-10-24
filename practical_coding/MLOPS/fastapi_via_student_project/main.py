from fastapi import FastAPI,Path,HTTPException,Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional
import json 


app =  FastAPI()



'''
Sequencing of numbers is given. Read the code as per the sequence. You will understand how to use Fast API. 
It may look very messy at first, but as you read point-wise, you will understand the basics of FastAPI. 


'''




def load_json():
    with open("data.json","r") as f:
        data = json.load(f)
    return data


def save_data(data_new):
    
    with open("data.json","w") as f:
        json.dump(data_new,f)
    
    
    

# <------- #1 ---------------> 

@app.get("/")
def home():
    return {"message":"hello world"}




# <---------------- #2 --------------> 
@app.get("/read")
def read():
    data =   load_json() # just loading a json file 
    return data 


'''
<------------- #3 ---------------------->
BOTH CAN BE USED BELOW | this is example of Path parameter 
patient_id : str
patient_id : str =  Path(...,description="provide the patient id",example="S001")

'''

@app.get("/patient/{patient_id}")
def get_patient_id(patient_id : str =  Path(...,description="provide the patient id",example="S001")):
    
    
    data  =  load_json()
    
    if patient_id in data :
        return data[patient_id]
    
    #return  {"error":"patient not found"}
    return HTTPException(status_code=404,detail="patiend not found")



'''
<------------- #4 ---------------------->
Query parameter to sort and order by values 

sort by :  age , physics , chem and maths marks 
order by :  asc or dec 

'''

@app.get("/sort")
def sort_data(sort_by : str  = Query(...,description="sort by age , physics , chemistry and maths marks"),
              order :str  =  Query(...,description="order in asc or desc format")):
    
    
    
    if not sort_by in ["age","physics","chemistry","maths"]:
        return HTTPException(status_code=400,detail="not in sorting field")
    
    if not order in ["asc","desc"]:
        return HTTPException(status_code=400,detail="not in order field")
    
    data = load_json()
    
    
    ## as it is copied line 

    sort_order = True if order=='desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    
    
    return sorted_data


'''
<------------- #5 ---------------------->
=> pydantic model introduction and integration 
=> Fast API automatically takes the Pydantic model as the blueprint of the object to be saved. 
=> use post method for creation 
=>  check creation on /docs 


'''


class Student(BaseModel):
    
    id :  str 
    name : str 
    age :  int  =  Field(gt=20,lt=40)
    physics:  float = Field(gt=0,lt=100)
    maths : float = Field(gt=0,lt=100)
    chemistry: float = Field(gt=0,lt=100)
    

class Student_update(BaseModel):

    name : Optional[str] 
    age :  Optional[int]  =  Field(gt=20,lt=40)
    physics:  Optional[float] = Field(gt=0,lt=100)
    maths :Optional [float] = Field(gt=0,lt=100)
    chemistry: Optional[float] = Field(gt=0,lt=100)
    
    
    
@app.post("/create")
def create(student : Student):
    
    data = load_json()
    
    if student.id in data:
        return HTTPException(status_code=400 , detail="Student already exists")
    
    
    data[student.id] =  student.model_dump(exclude=["id"])   
    
    save_data(data )  
    
    return JSONResponse(status_code=201, content={'message':'patient created successfully'})   


                     
                        
'''
<------------- #6 ---------------------->
=> update method

two method of updating 

1) Updating by putting the whole student ID model If you want to update the physics-only marks, then the whole data will be shown, and you just update the physics and execute it. 
2) Updating by sending only the physics marks means if you want to edit the physics marks, just send the key-value pair of it and update in the original one. 

Believe is the example of the first method. 

'''

@app.get("/edit/{patient_id}")
def update_patient(student_id:str,student:Student):
    
    data = load_json()
    
    if not student_id in data :
        raise HTTPException(status_code=404,detail=f"student  with id {student_id}  not found")   
    
    
    data[student_id] =  student.model_dump(exclude=["id"])
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={"message":"student successfully updated !"})    
    
    
    

    
    

'''
<------------- #7 ---------------------->
=> delete method  

'''
        
        
@app.delete('/delete/{student_id}')
def delete_student(student_id: str):

    # load data
    data = load_json()

    if student_id not in data:
        raise HTTPException(status_code=404, detail='Student not found')
    
    del data[student_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'Student deleted'})