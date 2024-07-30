 # Bankcrupty prediction using knn classifier model

This is a classification project, since the variable to predict is binary (bankruptcy or non-bankruptcy). The goal here is to model the probability that a business goes bankrupt from different features.
The data file contains 7 features about 250 companies
 
   ## Data Set Details:

The data set includes the following variables:

1.	industrial_risk: 0=low risk, 0.5=medium risk, 1=high risk.
2.	management_risk: 0=low risk, 0.5=medium risk, 1=high risk.
3.	financial flexibility: 0=low flexibility, 0.5=medium flexibility, 1=high flexibility.
4.	credibility: 0=low credibility, 0.5=medium credibility, 1=high credibility.
5.	competitiveness: 0=low competitiveness, 0.5=medium competitiveness, 1=high competitiveness.
6.	operating_risk: 0=low risk, 0.5=medium risk, 1=high risk.
7.	class: bankruptcy, non-bankruptcy (target variable).



The variables, or features, are the following:

    industrial_risk: 
	management_risk: 	
    financial flexibility: 
	credibility:
	competitiveness:
    operating_risk: 
	class(Y variable)

## requirements
blinker==1.8.2
click==8.1.7
colorama==0.4.6
Flask==3.0.3
importlib_metadata==8.0.0
itsdangerous==2.2.0
Jinja2==3.1.4
joblib==1.4.2
MarkupSafe==2.1.5
numpy==1.24.4
pandas==2.0.3
python-dateutil==2.9.0.post0
pytz==2024.1
scikit-learn==1.2.2
scipy==1.10.1
six==1.16.0
threadpoolctl==3.5.0
tzdata==2024.1
Werkzeug==3.0.3
zipp==3.19.2



## how to set up and execute-----

create virtual environment for installing only nessessary packages we needed and also for smooth running,

1. open anaconda promnt:-

    conda create -n bankcrupty python==3.8 -y     

2. go to the particular directory of the code and activate the environment by,

 conda activate bankcrupty
     
     

3. installing requried libraries by requirements.txt file,

    pip install -r requirements.txt

4. finally run the app.py in anaconda prompt by
    
    python app.py 

    (copy the localhost address and paste link on your google chrome and run)


try using different inputs inorder to predict the bankcrupty or Non-bankcrupty 


Author:
License This project is licensed under the MIT License. Feel free to use and modify the code as needed.

Contributor #bn

### THANK YOU FELLOW DEVELOPERS