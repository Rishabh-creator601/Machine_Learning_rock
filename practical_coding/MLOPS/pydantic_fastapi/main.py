from fastapi import FastAPI, Request, HTTPException,Path,Query
from fastapi.responses import JSONResponse
import json 
from user_model import User,User_Update

app =  FastAPI()




## normal api 
@app.get("/")
def hello():
    return JSONResponse(
        status_code=200,
        content={"message": "hello world "},
    )
    

def load_data():
    with open("users.json","r") as f:
        data  = json.load(f)
    return data 


def save_data(data):
    with open("users.json","w") as f:
        json.dump(data,f)
        


@app.get('/about')
def about():
    return JSONResponse(
        status_code=200,
        content={"message":"Hello world and fast api about "},
    )
    
    
## rendering json data with a specific id 
    
@app.get("/view/{user_id}")
def view_user(user_id  : str =  Path(...,description="Find user with a specific id ",example="U001")):
    
    data = load_data()
    
    if user_id in data.keys():
        return data[user_id]
    raise HTTPException(status_code=404,detail="User not found ")


## Query parameter 

@app.get("/sort")
def sort_data(sort_by : str =  Query(...,description="sort by age or Number of skills",example="sort_by=age"),
              order_by : str =  Query("asc",description="order by asc or desc ")):
    
    
    if sort_by not in ["age","n_skills"]:
        raise HTTPException(status_code=400,detail=f"sort_by not available with {sort_by}")
    
    if order_by  not in  ["asc","desc"]:
        raise  HTTPException(status_code=400,detail=f"Sorting not avaiable in {order_by} only in asc or desc")
    
    data =  load_data()
    for key,value in data.items():
        data[key]["n_skills"] = len(data[key]["skills"])
    
    order_by_key =  True if order_by =="desc" else False
    
    sorted_data =  sorted(data.values(),key =  lambda x : x.get(sort_by,0),reverse=order_by_key)
    
    return sorted_data


@app.post("/create")
def create_user(user :  User):
    
    data =  load_data()
    
    if user.id in data.keys():
        raise HTTPException(status_code=200,detail=f"User already exists with name : {user.name}")
    
    data[user.id] =  user.model_dump(exclude=["id"]) 
    save_data(data)   
    return JSONResponse(status_code=201,content={"message":f"User with name : {user.name} created "})



@app.put("/update/{user_id}")
def update_user(user_id :  str, new_user : User_Update):
    
    
    
    data =  load_data()
    
    if user_id not in data.keys():
        raise HTTPException(status_code=404,detail="User id Not exists ")
    
    new_data =  new_user.model_dump(exclude_unset=True)
    
    for key,value in new_data.items():
        data[user_id][key] = value 
        
        
    data[user_id]["id"] = user_id
    new_user_obj =  User(**data[user_id])
    new_updated_data =  new_user_obj.model_dump(exclude=["id"])
    
    data[user_id] =  new_updated_data
    
    save_data(data)
    
    return JSONResponse(status_code=201,content={"message":f"user with id {user_id} succesfully updated !"})




@app.delete("/delete_user")
def delete_user(user_id : str):
    
    data =  load_data()
    
    if user_id  not in data.keys():
        raise HTTPException(status_code=400,detail=f"User id : {user_id} not found ")
    
    del data[user_id]
    
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"user id deleted "})
    
        
    
    
    