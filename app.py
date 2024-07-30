from flask import Flask, request, render_template
import pickle
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier


app = Flask(__name__)

# Load the trained KNN model
with open('knn_model.pkl', 'rb') as model_file:
    knn_model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [
        float(request.form['industrial_risk']),
        float(request.form['management_risk']),
        float(request.form['financial_flexibility']),
        float(request.form['credibility']),
        float(request.form['competitiveness']),
        float(request.form['operating_risk'])
    ]

    input_data = pd.DataFrame([features])
    prediction = knn_model.predict(input_data)
        # If you need to decode the label
    prediction_label = prediction[0]
    result = 'Bankruptcy' if prediction_label == 1 else 'Non-Bankruptcy'
    
    # Convert features to numpy array
    #features_df= pd.DataFrame([features])
    # Make prediction
    #prediction = knn_model.predict(features_df)[0]
    #result = 'Bankruptcy' if prediction == 1 else 'Non-Bankruptcy'
    
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
