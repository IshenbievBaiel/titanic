from fastapi import FastAPI
import uvicorn
import joblib
from pydantic import BaseModel

model = joblib.load("titanik_model.pkl")
scaler = joblib.load("titanik_scaler.pkl")


titanic_app = FastAPI()

class TitanicSchema(BaseModel):
    Pclass: str
    Sex: str
    Fare: int
    FamilySize: bool
    Embarked: str




@titanic_app.post("/predict/")
async def titanic_predict(titanic: TitanicSchema):
    titanic_data = titanic.dict()

    new_gender = titanic_data.copy('Sex')
    gender_0_1 = [
        1 if new_gender == 'female' else 0,

    ]
    new_embarked = titanic_data.copy('Embarked')
    embarked_0_1 = [
        1 if new_embarked == 'Q' else 0,
        1 if new_embarked == 'S' else 0,
    ]

    data = list(titanic_data.values()) + gender_0_1 + embarked_0_1
    scaled_data = scaler.transform(data)
    pred = model.predict(scaled_data)[0]
    pred_label = {1:'Allive', 0:'No'}
    return{'Person': pred_label[pred]}

if __name__ == "__main__":
    uvicorn.run(titanic_app, host="127.0.0.1", port=8000)


