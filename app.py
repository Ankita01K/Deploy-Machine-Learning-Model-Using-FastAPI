# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:43:07 2024

@author: RAM_ANURAG
"""

import uvicorn 
from fastapi import FastAPI
from Placements import Placement
import numpy as np
import pickle
import pandas as pd

#create the app object
app= FastAPI()
pickle_in=open('model.pkl' ,'rb')
model=pickle.load(pickle_in)

#index route ,opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return{'message': 'welcome to learning fastAPI'}



@app.post('/predict')
def predict_placement(data:Placement):
    data=data.dict()
    #print(data)
    cgpa=data['cgpa']
    iq=data['iq']
   # print(model.predict([[cgpa,iq]]))
    prediction=model.predict([[cgpa,iq]])
    if prediction ==1:
        prediction='Placemnet Done'
    else:
        prediction='No Placement'
    return{
        'prediction': prediction
          }    
    
#run this API with unicorn
if __name__== '__main__':
    uvicorn.run(app ,host='127.0.0.1'  ,port=8000)
    
    
 #to run this use this commnand
#uvicorn app:app --reload  