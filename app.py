import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)
cursor = connection.cursor()

GET_AVERAGE_VALUES_FOR_MALE = '''
    SELECT
           AVG(air_pollution::int) as average_air_pollution,
           AVG(alcohol_use::int) as average_alcohol_use,
           AVG(dust_allergy::int) as average_dust_allergy,
           AVG(occupational_hazards::int) as average_occupational_hazards,
           AVG(genetic_risk::int) as average_genetic_risk,
           AVG(chronic_lung_disease::int) as average_chronic_lung_disease,
           AVG(balanced_diet::int) as average_balanced_diet,
           AVG(obesity::int) as average_obesity,
           AVG(smoking::int) as average_smoking,
           AVG(passive_smoker::int) as average_passive_smoker,
           AVG(chest_pain::int) as average_chest_pain,
           AVG(coughing_of_blood::int) as average_coughing_of_blood,
           AVG(fatigue::int) as average_fatigue,
           AVG(weight_loss::int) as average_weight_loss,
           AVG(shortness_of_breath::int) as average_shortness_of_breath,
           AVG(swallowing_difficulty::int) as average_swallowing_difficulty,
           AVG(clubbing_of_finger_nails::int) as average_clubbing_of_finger_nails,
           AVG(frequent_cold::int) as average_frequent_cold,
           AVG(dry_cough::int) as average_dry_cough,
           AVG(snoring::int) as average_snoring
    FROM cancer_patient_data_sets
    WHERE gender ~ '^\d+$' AND
    air_pollution ~ '^\d+$' AND
    alcohol_use ~ '^\d+$' AND
    dust_allergy ~ '^\d+$' AND
    occupational_hazards ~ '^\d+$' AND
    genetic_risk ~ '^\d+$' AND
    chronic_lung_disease ~ '^\d+$' AND
    balanced_diet ~ '^\d+$' AND
    obesity ~ '^\d+$' AND
    smoking ~ '^\d+$' AND
    passive_smoker ~ '^\d+$' AND
    chest_pain ~ '^\d+$' AND
    coughing_of_blood ~ '^\d+$' AND
    fatigue ~ '^\d+$' AND
    weight_loss ~ '^\d+$' AND
    shortness_of_breath ~ '^\d+$' AND
    swallowing_difficulty ~ '^\d+$' AND
    clubbing_of_finger_nails ~ '^\d+$' AND
    frequent_cold ~ '^\d+$' AND
    dry_cough ~ '^\d+$' AND
    snoring ~ '^\d+$' AND
    gender::int = 1
'''

GET_AVERAGE_VALUES_FOR_FEMALE = '''
    SELECT
           AVG(air_pollution::int) as average_air_pollution,
           AVG(alcohol_use::int) as average_alcohol_use,
           AVG(dust_allergy::int) as average_dust_allergy,
           AVG(occupational_hazards::int) as average_occupational_hazards,
           AVG(genetic_risk::int) as average_genetic_risk,
           AVG(chronic_lung_disease::int) as average_chronic_lung_disease,
           AVG(balanced_diet::int) as average_balanced_diet,
           AVG(obesity::int) as average_obesity,
           AVG(smoking::int) as average_smoking,
           AVG(passive_smoker::int) as average_passive_smoker,
           AVG(chest_pain::int) as average_chest_pain,
           AVG(coughing_of_blood::int) as average_coughing_of_blood,
           AVG(fatigue::int) as average_fatigue,
           AVG(weight_loss::int) as average_weight_loss,
           AVG(shortness_of_breath::int) as average_shortness_of_breath,
           AVG(swallowing_difficulty::int) as average_swallowing_difficulty,
           AVG(clubbing_of_finger_nails::int) as average_clubbing_of_finger_nails,
           AVG(frequent_cold::int) as average_frequent_cold,
           AVG(dry_cough::int) as average_dry_cough,
           AVG(snoring::int) as average_snoring
    FROM cancer_patient_data_sets
    WHERE gender ~ '^\d+$' AND
    air_pollution ~ '^\d+$' AND
    alcohol_use ~ '^\d+$' AND
    dust_allergy ~ '^\d+$' AND
    occupational_hazards ~ '^\d+$' AND
    genetic_risk ~ '^\d+$' AND
    chronic_lung_disease ~ '^\d+$' AND
    balanced_diet ~ '^\d+$' AND
    obesity ~ '^\d+$' AND
    smoking ~ '^\d+$' AND
    passive_smoker ~ '^\d+$' AND
    chest_pain ~ '^\d+$' AND
    coughing_of_blood ~ '^\d+$' AND
    fatigue ~ '^\d+$' AND
    weight_loss ~ '^\d+$' AND
    shortness_of_breath ~ '^\d+$' AND
    swallowing_difficulty ~ '^\d+$' AND
    clubbing_of_finger_nails ~ '^\d+$' AND
    frequent_cold ~ '^\d+$' AND
    dry_cough ~ '^\d+$' AND
    snoring ~ '^\d+$' AND
    gender::int = 2
'''

connection.commit()

@app.get("/")
def home():
    return render_template('index.html')

@app.get("/data.html")
def view_database():
    cursor.execute("SELECT * FROM cancer_patient_data_sets")
    data = cursor.fetchall()
    # print(data)
    return render_template('data.html', data=data)

@app.get("/ages-20-to-40.html")
def compare_age_20_to_40():
    ages = []
    level = []
    processed_data = {}

    cursor.execute('''
            SELECT age, level
            FROM cancer_patient_data_sets
            WHERE age ~ '^\d+$'  -- Matches only numeric values
            AND age::int BETWEEN 20 AND 40
            ORDER BY age ASC;
            ''')
    data = cursor.fetchall()
    for record in data:
        ages.append(record[0])
        level.append(record[1])
        
    unique_ages = set(ages)
    for a in unique_ages:
        processed_data[a] = {"Low": 0, "Medium": 0, "High": 0}
        
    for i in range(len(ages)):
        processed_data[ages[i]][level[i]] += 1

    return render_template('ages-20-to-40.html', processed_data=processed_data)

@app.get("/male-vs-female.html")
def male_vs_female_comparison():
    cursor.execute(GET_AVERAGE_VALUES_FOR_MALE)
    averageMaleData = cursor.fetchall()
    
    cursor.execute(GET_AVERAGE_VALUES_FOR_FEMALE)
    averageFemaleData = cursor.fetchall()
    return render_template('male-vs-female.html', averageMaleData=averageMaleData, averageFemaleData=averageFemaleData)

if __name__ == "__main__":
    print("hello world")