import pandas as pd 
from returns.result import Success,Failure,Result
import os ,sys 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.base import BaseEstimator
from sklearn.svm  import SVC
from typing import Literal
from functools import partial




"""

DEVELOPMENT GRADE FUNCTION 


1)  each parameter has data type and can have default values 
2)  each parameter has success or failed result ,either message or in progress 
3)  minimum hardcoded values 
4)  each function has max 2 work and main work under try except 
5)  each function knows what is getting returned ->  ?  
6)  if multiple objects are returning make a data class for it 

 
Prerequisites :  dataclasses , returns Result [success,failure]

"""

@dataclass
class DataSplit:
    x_train :  pd.DataFrame
    x_test :  pd.DataFrame
    y_train :  pd.Series
    y_test :  pd.Series



@dataclass
class Model:
    model_name  :  str 
    model :  BaseEstimator  
    score :  float 
    
    
    

def load_data(path: str ,filename: str ) ->  Result[pd.DataFrame,str]:
    
    try  :
        file =  os.path.join(path,filename)
        
        if file.endswith(".csv"):
            data =  pd.read_csv(file)
            return Success(data)
        else:
            return Failure(f"file should be a csv file and not {file.split('.')[-1]} ")
    except FileNotFoundError:
        return Failure(f"file :{filename} does not exist")
    



def split_data(data :  pd.DataFrame, 
               test_size : float =0.2,
               random_state : int =42,
               target_column : str ="target") -> Result[DataSplit,str]:
    
    
    # test_size =  0.3  if test_size >  0.3 else test_size 
    if not 0 < test_size <= 0.3:
        return Failure("Test size must be in range 0-0.3 ")
    

        
    try : 
    
        x =  data.drop(columns=[target_column])
        y =  data[target_column]
        
        x_train,x_test,y_train,y_test =  train_test_split(x,y,test_size=test_size,random_state=random_state)
        splitted_data =  (x_train,x_test,y_train,y_test)

    except Exception as e : 
        
        return Failure(f"Data cannot be spliited ! due to {e}")
    
    return Success(DataSplit(*splitted_data))




model_names = Literal["lr","svc","rf"]

def train_model(values : DataSplit,model_name : model_names ) -> Result[Model,str]:
    
    rf =  RandomForestClassifier()
    lr =  LogisticRegression()
    svc =  SVC()
    models = {"lr":lr,"svc":svc,"rf":rf}
    
    if not model_name in list(models.keys()):
        return Failure(f"model must be  in these : {model_names}")
    
    try : 
        model =  models[model_name]
        model.fit(values.x_train,values.y_train)
        score =  model.score(values.x_test,values.y_test)
        
    except Exception as e :
        return Failure(f"model could not be trained due to  {e}")
        
    return Success(Model(model_name,model,score))
    
    
    
    

'''

why not raising a error in match result Model(....)

Those variables don’t need to exist beforehand because case creates them. 
In a case pattern, a plain name is called a capture pattern, and it means “if this matches, 
store the value in this variable.” Python assigns to the name rather than reading it, 
just as x = 5 works without x already existing.

'''

        
def main() -> None:
    result = (
        load_data(".", "data.csv")
        .bind(split_data)
        .bind(partial(train_model, model_name="svc"))
    )

    match result:
        case Success(Model(model_name,model, score)):
            print(f"Trained {model} with accuracy {score:.3f}")
        case Failure(error):
            print(f"Pipeline failed: {error}")
            sys.exit(1)


if __name__ == "__main__":
    main()
