import joblib as jbl
import uvicorn

from schema import Prediction_response

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from fastapi import Query

from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler


app = FastAPI()

regresor_utils = jbl.load('bin/regresor_utils_.joblib')

@app.get('/', status_code=status.HTTP_200_OK, tags=['Root'])
def root():
    return JSONResponse(content={'msj': 'HOME ROUTE'})

@app.get('/predict/', tags=['Predicciones'], response_model=Prediction_response)
def predict(p: int = Query(..., title='Puntos', description='Puntos a predecir por medio del regresor', le=7, gt=0)):
    '''
    Permite realizar predicciones sobre la serie de tiempo P puntos (días)
    en el futuro.
    Cada vez que se hagan predicciones, dichos resultados se actualizarán
    como datos de la serie, es decir, repetidas ejecuciones del endpoint
    harán que los se prediga nuevos puntos sobre los puntos ya predichos
    por el regresor
    '''
    predicciones = [0 for i in range(p)]
    for dato in range(0,p):

        esc_data = regresor_utils['scaler'].transform(regresor_utils['window_data']).reshape(1,-1)
        pred_esc = regresor_utils['regresor'].predict(esc_data).reshape(-1,1)
        pred_esc = regresor_utils['scaler'].inverse_transform(pred_esc)

        predicciones[dato] = pred_esc[0,0]

        regresor_utils['window_data'][:-1] = regresor_utils['window_data'][1:]
        regresor_utils['window_data'][-1] = float(pred_esc[0])
    
    return Prediction_response(prediction=predicciones)
    
""" if __name__ == '__main__':
    uvicorn.run(app) """



