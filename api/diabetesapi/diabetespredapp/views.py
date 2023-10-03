from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import joblib
import numpy as np
from .models import Prediction  


class PredictionView(APIView):
    def post(self, request):
        try:
            # Load the trained model
            model = joblib.load('/Users/Tuntu/Desktop/PJ/diabetes_prediction/Diabetes-Prediction-API/model/diabetes_model.joblib')

            # Get input data 
            input_data = request.data.get('input_data')  

            # predictions
            predicted_value = model.predict(np.array(input_data).reshape(1, -1))

            # save it to the database
            prediction = Prediction(
                age=input_data[0],
                sex=input_data[1],
                bmi=input_data[2],
                bp=input_data[3],
                s1=input_data[4],
                s2=input_data[5],
                s3=input_data[6],
                s4=input_data[7],
                s5=input_data[8],
                s6=input_data[9],


                predicted_value=predicted_value[0]
            )
            prediction.save()

            # Return the predicted value in the API response
            return Response({'predicted_value': predicted_value[0]}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
