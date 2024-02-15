# Lung Cancer Dataset
## **About this [dataset](https://www.kaggle.com/datasets/thedevastator/cancer-patients-and-air-pollution-a-new-link?resource=download)**
This dataset contains information on patients with lung cancer, including their age, gender, air pollution exposure, alcohol use, dust allergy, occupational hazards, genetic risk, chronic lung disease, balanced diet, obesity, smoking, passive smoker, chest pain, coughing of blood, fatigue, weight loss ,shortness of breath ,wheezing ,swallowing difficulty ,clubbing of finger nails and snoring.

## **Description**
This repository serves as a platform for exploring database and web application development. Some of the examples for chartJS I've implemented are Bar Charts, and Polar Area Charts. This helps user to visualize their data in a clearer view after extracting from a database.

<img width="1440" alt="Screenshot 2024-02-15 at 5 37 48 PM" src="https://github.com/jarelloy/cancer-patient-data/assets/72366471/bfbe8f27-7980-4f16-8cda-be6d63320e5a">

<img width="828" alt="Screenshot 2024-02-15 at 5 39 30 PM" src="https://github.com/jarelloy/cancer-patient-data/assets/72366471/4f267517-ada8-4dd9-8fd3-c20c5c0c2770">


## **Learning Points**
- Database: I've learnt how to create a database, and various SQL Queries that allow me to manipulate the database, or retrieve necessary information needed.
- ReactJS: I've learnt how to use ReactJS, more importantly ChartJS to display various types of charts for analyzing purposes.
- Python: I've learnt how to code better with Python, understanding the syntax better and opening a web socket with Python, rendering templates to deploy a web application
  

## How to Run
Follow these steps to run the application locally:
- Create a `.env` file in the project root directory with the following content:
```
FLASK_APP=app
FLASK_DEBUG=True
FLASK_ENV=development
DATABASE_URL="postgres://remqzgvs:ZSBTnK0WhaHqGuKN4AR8T8k9Bb9jB9sr@rain.db.elephantsql.com/remqzgvs"
```
Replace DATABASE_URL with your actual postgreSQL URL. For me, I'm using ElephantSQL which is a free to use Database for learning purposes. Feel free to use my database!

- Open a terminal and run the following command: `flask run`
- Open your web browser and navigate to 127.0.0.1:5000
  
License
This project is licensed under the MIT License. Feel free to use and modify the code for your needs.

Enjoy exploring new music with the Playlist Generator! 🎶
