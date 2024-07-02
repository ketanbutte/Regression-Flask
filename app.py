from flask import Flask,render_template,request #imported flask class
import pickle
import numpy as np

model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__) #instance of the class will be our WSGI application

#what is WSGI application
# --> It stands for Web Server Gateway Interface

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict_charges():
    age = int(request.form.get('age'))
    bmi = float(request.form.get('bmi'))
    gender = request.form.get('gender')
    smoker = request.form.get('smoker')

    if gender =='female':
        sex_female = 1
        sex_male = 0
    else:
        sex_female = 0
        sex_male = 1

    if smoker =='no':
        smoker_no = 1
        smoker_yes = 0
    else:
        smoker_no = 0
        smoker_yes =1


    # prediction
    result = model.predict(np.array([age,bmi,sex_female,sex_male,smoker_no,smoker_yes]).reshape(1,6))

    # if result[0] == 1:
    #     result = 'placed'
    # else:
    #     result = 'not placed'

    return render_template('index.html',result=round(result[0]))