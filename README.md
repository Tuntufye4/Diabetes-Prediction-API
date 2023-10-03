# Diabetes-Prediction-API

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Example Usage](#example-usage)
- [Machine Learning Model](#machine-learning-model)




## Project Description

The Diabetes Prediction API is a machine learning project that predicts diabetes based on input features. It uses a trained machine learning model to make predictions and provides a REST API for easy integration into applications.

## Features

- Predicts diabetes based on input features.
- Provides an easy-to-use REST API for making predictions.
- Stores prediction results in a database for future reference.

## Getting Started


### Prerequisites


- Python 3.8+
- django
- django rest-framework
- Scickit-learn
- httpie 

### Installation

1. Clone the repository:

   ```bash
   git clone  https://github.com/Tuntufye4/Diabetes-Prediction-API.git

## Machine Learning Model

## Usage

### Example Usage

1. Start the development server:

   ```bash
   python manage.py runserver

2. Create an input.json file

   example:
   ```bash

   {
    "input_data": [0.025, 0.04, 0.106, 0.215, -0.4612, -0.712, 0.539, -0.036, 0.128, 0.781]
   }


4. Run the below command in httpie to add the input json file

   ```bash
   http POST http://localhost:8000/api/predict/ < input.json


4. The command above should give you this output:

   ```bash

   HTTP/1.1 200 OK
   Allow: POST, OPTIONS
   Content-Length: 36
   Content-Type: application/json
   Cross-Origin-Opener-Policy: same-origin
   Date: Tue, 03 Oct 2023 15:39:36 GMT
   Referrer-Policy: same-origin
   Server: WSGIServer/0.2 CPython/3.8.0
   Vary: Cookie
   X-Content-Type-Options: nosniff
   X-Frame-Options: DENY

   {
     "predicted_value": 546.027883704299
   }  

   







 
