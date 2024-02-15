import csv
import os
import psycopg2
from psycopg2 import IntegrityError

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor()

CREATE_DATABASE_TABLE = """
    CREATE TABLE IF NOT EXISTS cancer_patient_data_sets (
        index TEXT,
        patient_id TEXT,
        age TEXT,
        gender TEXT,
        air_pollution TEXT,
        alcohol_use TEXT,
        dust_allergy TEXT,
        occupational_hazards TEXT,
        genetic_risk TEXT,
        chronic_lung_disease TEXT, 
        balanced_diet TEXT,
        obesity TEXT,
        smoking TEXT,
        passive_smoker TEXT,
        chest_pain TEXT,
        coughing_of_blood TEXT,
        fatigue TEXT,
        weight_loss TEXT,
        shortness_of_breath TEXT,
        wheezing TEXT,
        swallowing_difficulty TEXT,
        clubbing_of_finger_nails TEXT,
        frequent_cold TEXT,
        dry_cough TEXT,
        snoring TEXT,
        level TEXT
    )
"""

cursor.execute(CREATE_DATABASE_TABLE)

with open('cancer patient data sets.csv', 'r') as file:
    reader = csv.reader(file)
    # next(reader)
    for (row) in reader:
        try:
            print(row)
            cursor.execute("""
                INSERT INTO cancer_patient_data_sets (index, patient_id, age, gender, air_pollution, alcohol_use, dust_allergy, occupational_hazards, genetic_risk, chronic_lung_disease, balanced_diet, obesity, smoking, passive_smoker, chest_pain, coughing_of_blood, fatigue, weight_loss, shortness_of_breath, wheezing, swallowing_difficulty, clubbing_of_finger_nails, frequent_cold, dry_cough, snoring, level)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, row)
        except IntegrityError as e: 
            print(e)
            pass