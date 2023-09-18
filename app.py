from flask import Flask, request
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route('/', methods=['POST'])
def index():
    request_data = request.get_json()
    loaded_model = joblib.load('l_model.pkl')
    data = {key: value for key, value in request_data.items()}
    data_dict = {key: value[0] for key, value in data.items()}
    data_list = list(data_dict.values())
    data_array = np.array([data_list])
    pre = loaded_model.predict(data_array)
    return f'{pre[0]}'

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, request
# import joblib
# import numpy as np
# app = Flask(__name__)

# @app.route('/', methods=['POST'])
# def index():
#     request_data = request.get_json()
#     loaded_model = joblib.load('model.pkl')

#     user_data = {}

#     user_data['CreditScore'] = [int(request_data.get("CreditScore", 0))]
#     user_data['Age'] = [int(request_data.get("Age", 0))]
#     user_data['Tenure'] = [float(request_data.get("Tenure", 0))]
#     user_data['Balance'] = [float(request_data.get("Balance", 0))]

#     user_data['HasCrCard'] = [float(request_data.get("HasCrCard", 0))]
#     user_data['IsActiveMember'] = [float(request_data.get("IsActiveMember", 0))]
#     user_data['EstimatedSalary'] = [float(request_data.get("EstimatedSalary", 0))]


#     gen = request_data.get("Gender", "")

#     if(gen  == 'Male'):
#         user_data['Male'] = [1] 
#         user_data['Female'] = [0] 
        
#     if(gen == 'Female'):
#         user_data['Male'] = [0] 
#         user_data['Female'] = [1]


#     if(int(request_data.get("NumOfProducts", 0) == 1)):
#         user_data['NumOfProducts_1'] = [1] 
#         user_data['NumOfProducts_2'] = [0]  
#         user_data['NumOfProducts_3'] = [0]
#         user_data['NumOfProducts_4'] = [0]

#     elif(int(request_data.get("NumOfProducts", 0) == 2)):
#         user_data['NumOfProducts_1'] = [0]
#         user_data['NumOfProducts_2'] = [1] 
#         user_data['NumOfProducts_3'] = [0] 
#         user_data['NumOfProducts_4'] = [0]

#     elif(int(request_data.get("NumOfProducts", 0) == 3)):
#         user_data['NumOfProducts_1'] = [0]
#         user_data['NumOfProducts_2'] = [0] 
#         user_data['NumOfProducts_3'] = [1] 
#         user_data['NumOfProducts_4'] = [0] 

#     elif(int(request_data.get("NumOfProducts", 0) == 4)):
#         user_data['NumOfProducts_1'] = [0]
#         user_data['NumOfProducts_2'] = [0] 
#         user_data['NumOfProducts_3'] = [0] 
#         user_data['NumOfProducts_4'] = [1] 
           
       
#     geo = request_data.get("Geography", "") 
#     if(geo == 'France'):
#         user_data['France'] = [1]
#         user_data['Spain'] = [0]
#         user_data['Germany'] = [0] 

#     elif(geo == 'Spain'):
#         user_data['France'] = [0]
#         user_data['Spain'] = [1]
#         user_data['Germany'] = [0] 
         
#     elif(geo  == 'Germany' ):
#         user_data['France'] = [0]
#         user_data['Spain'] = [0]
#         user_data['Germany'] = [1] 

#     data_dict = {key: value[0] for key, value in user_data.items()}
#     data_list = list(data_dict.values())
#     data_array = np.array([data_list])
#     print(data_array)
#     pre = loaded_model.predict(data_array)
#     return f'Hello, {pre}!'

# if __name__ == '__main__':
#     app.run(debug=True)