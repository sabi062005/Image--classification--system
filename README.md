# Image Classification System Using Python

## About

This project is an image classification system developed using Python, TensorFlow, Keras, and Flask. The system classifies uploaded images into four predefined categories: Plastic, Paper, Metal, and Glass.

A Convolutional Neural Network (CNN) is trained using a labeled image dataset. Users can upload an image through a web interface, and the trained model predicts the category of the image.

## Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Pillow
- Flask
- HTML
- CSS
- Git
- GitHub

## Categories

The system classifies images into the following categories:

1. Plastic
2. Paper
3. Metal
4. Glass

## Features

- Upload an image through a web interface
- Image preprocessing and resizing
- CNN-based image classification
- Prediction of predefined categories
- Flask-based web application
- Simple and user-friendly interface

## Project Structure

```text
image-classification-system/
│
├── dataset/
│   ├── Plastic/
│   ├── Paper/
│   ├── Metal/
│   └── Glass/
│
├── model/
│   └── image_classifier.keras
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── app.py
├── train.py
├── requirements.txt
├── .gitignore
└── README.md

How the Project Works:

User uploads an image
        ↓
Flask receives the image
        ↓
Image preprocessing
        ↓
Trained CNN model
        ↓
Prediction
        ↓
Plastic / Paper / Metal / Glass

How to Run:

1. Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL

2. Open the Project Folder
cd image-classification-system

3. Create a Virtual Environment
python -m venv venv

4. Activate the Virtual Environment
For Windows:
venv\Scripts\activate

5. Install Required Libraries
pip install -r requirements.txt

6. Train the Model
python train.py
The trained model will be saved locally in the model folder.

7. Run the Flask Application
python app.py
Open the application in a browser:
http://127.0.0.1:5000

Prediction:

Open the web application.
Click Choose File.
Select an image.
Click Predict.
The predicted category will be displayed.
Example:
Uploaded Image → Plastic

Future Improvements:

Increase the size and variety of the dataset
Improve classification accuracy
Add more categories
Display prediction confidence
Improve the web interface
Deploy the application online

Author:
Developed as a Python and Machine Learning project.
