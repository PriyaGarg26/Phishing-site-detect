import uvicorn
from fastapi import FastAPI
import joblib,os
import pickle

#create the app object
app = FastAPI()

#pkl
phish_model = open('phishing.pkl','rb')
phish_model_ls = pickle.load(phish_model)

# ML Aspect
@app.get('/')
def index():
    return {'message':'Welcome,To,Phishing,Site,Prediction'}
@app.get('/predict/{feature}')
async def predict_site(features):
	X_predict = []
	X_predict.append(str(features))
	y_Predict = phish_model_ls.predict(X_predict)
	if y_Predict == 'bad':
		result = "This is a Phishing Site"
	else:
		result = "This is not a Phishing Site"

	return {
        (features, result) 
        }

if __name__ == '__main__':
	uvicorn.run(app,host="127.0.0.1",port=8000)

#uvicorn app:app --reload

