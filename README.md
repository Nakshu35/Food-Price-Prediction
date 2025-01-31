# 🍕 Food Price Detection 🍔

Welcome to the **Food Price Detection** project! This project aims to predict the price of food items based on various features using machine learning. The project includes a Flask-based local application for predicting food prices.

## 🚀 Features

- **Food Price Prediction**: Predict the price of food items based on input features.
- **Local Flask App**: A simple local web interface built with Flask for testing predictions.
- **Dataset**: Includes a dataset for training and testing the model.

## 📂 Project Structure
food-price-detection/
├── app.py # Flask application for local predictions
├── templates/ # HTML templates for the local web interface
│ └── index.html # Main page for input and prediction
├── static/ # Static files (CSS, JS, images)
├── dataset/ # Dataset used for training the model
│ └── food_data.csv # Sample dataset
├── models/ # Trained models
├── requirements.txt # Python dependencies
├── LICENSE # License file
└── README.md # This file

## 🛠️ Installation

1. **Clone the repository**:
git clone https://github.com/your-username/food-price-detection.git
cd food-price-detection

Install dependencies:
pip install -r requirements.txt

Run the Flask application:
python app.py

Access the local application:
Open your browser and go to http://127.0.0.1:5000/process


🧑‍💻 Usage
Input Food Details: Enter the details of the food item in the local web form.

Get Price Prediction: Click on the "Predict" button to get the estimated price.

📊 Dataset
The dataset used in this project is located in the dataset/ directory. It contains various features related to food items and their corresponding prices.

🤖 Model
The model used for price prediction is trained using the dataset provided. The model is built using XGBoost and other machine learning libraries. You can find the trained model in the models/ directory.

📝 Requirements
The required Python libraries are listed in requirements.txt. Install them using:
pip install -r requirements.txt

📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Acknowledgments
Thanks to the creators of the dataset used in this project.

Special thanks to the open-source community for providing excellent libraries like Flask, Scikit-learn, and XGBoost.

📧 Contact
If you have any questions or suggestions, feel free to reach out:

Your Name - nakshuwork2@gmail.com

Project Link: https://github.com/Nakshu35/Food-Price-Prediction

Happy coding! 🎉