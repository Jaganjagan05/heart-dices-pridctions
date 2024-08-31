from flask import Flask, render_template, request
import pickle
import numpy as np

model1 = pickle.load(open(r'C:\Users\majag\OneDrive\Desktop\heart\model\jagan.pickle','rb'))  

app = Flask(__name__)  # initializing Flask app


@app.route("/",methods=['GET'])
def hello():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST': 

        d1 = request.form['age']
        d2 = request.form['sex']
        d3 = request.form['Chest pain type']
        d4 = request.form['BP']
        d5 = request.form['chol']
        d6 = request.form['fbs']
        d7 = request.form['EKG results']
        d8 = request.form['Max HR']
        d9 = request.form['Exercise angina']
        d10 = request.form['ST depression']
        d11= request.form['Slope of ST']
        d12 = request.form['Number of vessels fluro']
        d13 = request.form['Thallium']
        
        
        

        arr = np.array([[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13]])
        print([d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13])
        pred1 = model1.predict(arr)
        print(pred1)

    return render_template('result.html',prediction_text1=pred1)
    
if __name__ == '__main__':
    app.run(debug=True)
    
#app.run(host="0.0.0.0")            # deploy
            # run on local system
