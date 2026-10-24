import streamlit as st 
import pickle,requests
import pandas as pd

@st.cache_resource
def load_model():
    
    model = pickle.load(open("models/model.pkl","rb"))
    return model 
 

model =  load_model()
API_URL =  " http://127.0.0.1:8000/predict"


if "model" not in st.session_state:
    st.session_state["model"] = model 



st.title("Make Some Predictions")

bedrooms =  float(st.slider("Choose No OF Bedrooms",2,9,5))
bathrooms =  float(st.slider("Choose No of Bathrooms",2,8,6))
sqft_living  = st.number_input( "Insert The area of Living Room (in square feet)",value=500, placeholder="min : 400 max: 13000",min_value=370,max_value=13540)
sqft_basement  = st.number_input( "Insert The area of Basement  (in square feet)",value=500, placeholder="min : 0 max: 4800",min_value=0,max_value=4800)
floors = float(st.slider("Enter No of Floors",2,4,3))
view = st.slider("How much do you want to rate the view ?",2,4,2)
condition = st.slider("How much do you want to rate the condition of the house ?",2,5,3)




values = [bedrooms,bathrooms,sqft_living,floors,view,condition,sqft_basement]

model = st.session_state["model"]

if st.button("Predict"):
    
    input_data = {
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "sqft_living": sqft_living,
        "floors": floors,
        "view": view,
        "condition": condition,
        "sqft_basement": sqft_basement
    }
    
    
    try : 
        response  = requests.post(API_URL,json=input_data)
        result =  response.json()
        
        print(result)
        
        if response.status_code == 200 and "predicted_price" in result:
            prediction = result["predicted_price"]
            st.success(f"Predicted Price: **{prediction}**")

    
    
    except:
        st.write("error in processing document ")
             
             
        

















