import streamlit as st
import requests

api_url = 'http://127.0.0.1:8000/predict'

st.title('Titanic')

class_titan = st.number_input('Класс', min_value=0)
gen_titan = st.selectbox('Пол', ['male', 'female'])
age_titan = st.number_input('Возраст', min_value=0, step=5)
fare_titan = st.number_input('Fare')
family_titan = st.number_input('Семья в титанике', min_value=0)
embar_titan = st.selectbox('Порт', ['Embarked_C', 'Embarked_Q', 'Embarked_S'])



titanic_made = {
    'Pclass': class_titan,
    'Sex': gen_titan,
    'Age': age_titan,
    'Fare': fare_titan,
    'FamilySize': family_titan,
    'Embarked': embar_titan
}

if st.button('Предсказать'):
    try:
        titan = requests.post(api_url, json=titanic_made, timeout=10)
        if titan.status_code == 200:
            result = titan.json()
            st.success(f'Result {result.get('Person')}')
        else:
             st.error(f'Ошибка: {titan.status_code}')

    except requests.exceptions.RequestException:
        st.error(f'Не удалось соединиться с API')