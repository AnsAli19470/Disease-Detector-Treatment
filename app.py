import streamlit as st
import pickle
import numpy as np
import pandas as pd
import ast
from difflib import get_close_matches
import warnings

warnings.filterwarnings("ignore", message="X does not have valid feature names")

# --- Utility Function ---
def get_closest_symptom(symptom, symptoms_list):
    matches = get_close_matches(symptom, symptoms_list, n=1, cutoff=0.6)
    return matches[0] if matches else None

# --- Load Resources ---
svc = pickle.load(open('svc.pkl', 'rb'))
sym_des = pd.read_csv('symtoms_df.csv')
diets = pd.read_csv('diets.csv')
workout = pd.read_csv('workout_df.csv')
description = pd.read_csv('description.csv')
medications = pd.read_csv('medications.csv')
precautions = pd.read_csv('precautions_df.csv')

# --- Mappings ---
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5, 'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11, 'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16, 'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21, 'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26, 'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32, 'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37, 'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42, 'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46, 'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50, 'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55, 'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59, 'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64, 'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69, 'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73, 'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77, 'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82, 'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86, 'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90, 'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94, 'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99, 'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103, 'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108, 'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111, 'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115, 'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118, 'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122, 'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127, 'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131}
diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}

# --- Prediction ---
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1
    return diseases_list[svc.predict([input_vector])[0]]

def helper(dis):
    desc = " ".join(description[description['Disease'] == dis]['Description'].astype(str).values)
    pre = precautions[precautions['Disease'] == dis][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values.tolist()
    med = medications[medications['Disease'] == dis]['Medication'].values.tolist()
    die = diets[diets['Disease'] == dis]['Diet'].values.tolist()
    wrkout = workout[workout['disease'] == dis]['workout'].values.tolist()
    return desc, pre, med, die, wrkout

# --- UI ---
st.markdown("<h1 style='text-align: center; color: #4B9CD3;'>🩺 Smart Disease Prediction System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your symptoms to predict possible disease and get personalized medical recommendations.</p>", unsafe_allow_html=True)

# Input Box
with st.container():
    user_symptoms = st.text_input("📝 Enter Symptoms (comma-separated)", placeholder="e.g. headache, fever, cough")

# --- Predict Button ---
if st.button("🔍 Predict Disease"):
    if user_symptoms.strip():
        raw_symptoms = [s.strip().lower().replace(" ", "_") for s in user_symptoms.split(",")]
        corrected_symptoms = []
        invalid = []

        for symptom in raw_symptoms:
            match = get_closest_symptom(symptom, symptoms_dict.keys())
            if match:
                corrected_symptoms.append(match)
            else:
                invalid.append(symptom)

        if invalid:
            st.error(f"❌ Unrecognized symptoms: {', '.join(invalid)}")
        else:
            # Matched Symptoms
            with st.container():
                st.markdown("### ✔️ Matched Symptoms")
                for original, corrected in zip(raw_symptoms, corrected_symptoms):
                    st.markdown(f"<span style='color:green'>`{original}` → **{corrected}**</span>", unsafe_allow_html=True)

            # Prediction
            predicted_disease = get_predicted_value(corrected_symptoms)
            desc, pre, med, die, wrkout = helper(predicted_disease)

            # Results Section
            with st.container():
                st.markdown("---")
                st.markdown(f"<h2 style='color:#4B9CD3;'>🧾 Predicted Disease: <span style='color:#2E8B57'>{predicted_disease}</span></h2>", unsafe_allow_html=True)
                st.markdown("<hr>", unsafe_allow_html=True)

                # Expandable sections for detailed info
                with st.expander("🩻 Description"):
                    st.markdown(f"<div style='padding:5px 10px;background-color:2E8B57#;border-radius:8px'>{desc}</div>", unsafe_allow_html=True)

                with st.expander("🔐 Precautions"):
                    for item in pre[0]:
                        if pd.notna(item):
                            st.write(f"• {item}")

                with st.expander("💊 Medications"):
                    for item in ast.literal_eval(med[0]):
                        st.write(f"• {item}")

                with st.expander("🏃 Lifestyle Tips"):
                    for item in wrkout:
                        st.write(f"• {item}")

                with st.expander("🥗 Recommended Diet"):
                    for item in ast.literal_eval(die[0]):
                        st.write(f"• {item}")
    else:
        st.warning("⚠️ Please enter symptoms before predicting.")
