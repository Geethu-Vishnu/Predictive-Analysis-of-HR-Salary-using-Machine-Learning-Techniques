from flask import Flask ,render_template , request , jsonify
import numpy as np
import pickle


app = Flask(__name__)

# Define attribute dictionaries

workclass_dict = {'Federal-gov':0,'Local-gov':1,'Never-worked':2,'Private':3,'Self-emp-inc':4,'Self-emp-not-inc':5,'State-gov':6,'Without-pay':7,'Other':8}
education_dict = {'10th':0,'11th':1,'12th':2,'1st-4th':3,'5th-6th':4,'7th-8th':5,'9th':6,'Assoc-acdm':7,'Assoc-voc':8,'Bachelors':9,'Doctorate':10,'HS-grad':11,'Masters':12,'Preschool':13,'Prof-school':14,'Some-college':15}
occupation_dict = {'Adm-clerical':0,'Armed-Forces':1,'Craft-repair':2,'Exec-managerial':3,'Farming-fishing':4,'Handlers-cleaners':5,'Machine-op-inspct':6,'Other-service':7,'Priv-house-serv':8,'Prof-specialty':9,'Protective-serv':10,'Sales':11,'Tech-support':12,'Transport-moving':13}
sex_dict= {'Female':0,'Male':1}

# Load logistic regression model:
model = pickle.load(open('model.pkl','rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    


    # Available Options
    #education = ['10th','11th','12th','1st-4th','5th-6th','7th-8th','9th','Assoc-acdm','Assoc-voc','Bachelors','Doctorate','HS-grad','Masters','Preschool','Prof-school','Some-college']
    #workclass = ['Federal-gov','Local-gov','Never-worked','Private','Self-emp-inc','Self-emp-not-inc','State-gov','Without-pay','Other']
    #occupation = ['Adm-clerical','Armed-Forces','Craft-repair','Exec-managerial','Farming-fishing','Handlers-cleaners','Machine-op-inspct','Other-service','Priv-house-serv','Prof-specialty','Protective-serv','Sales','Tech-support','Transport-moving']
    #sex = ['Female','Male']



    # Getting the input data from the form

    if request.method == 'POST':
        age = request.form['age']
        workclass_val = request.form['workclass']
        education_val = request.form['education']
        occupation_val = request.form['occupation']
        sex_val = request.form['sex']
        hours_per_week = request.form['hours_per_week']
        try:
            age = int(age)
            hours_per_week = int(hours_per_week)
            if age < 17 or hours_per_week < 0:
                raise ValueError
        except ValueError:
            return render_template('index.html', message="Please enter a valid age and hours_per_week (age must be atleast 17 and hours per week must be non-negative).")
        

        workclass = workclass_dict.get(workclass_val,-1)
        education= education_dict.get(education_val,-1)
        occupation = occupation_dict.get(occupation_val,-1)
        sex = sex_dict.get(sex_val,-1)

        if -1 in [workclass , education , occupation , sex]:
            return render_template('index.html',message="Invalid value for one or more attributes .")
        

        
    


    

        arr = np.array([[age,workclass,education,occupation,sex,hours_per_week]])

        # Making Prediction :
        pred = model.predict(arr)

        # Convert prediction to salary category

        if pred == 0:
            salary = "<=50K"
        else:
            salary = ">=50K"

        # Display the predicted salary on the results page
        return render_template('index.html', data=salary)
    
    
    

    



    
    

# Run the application

if __name__ == '__main__':
    app.run(debug=True)







