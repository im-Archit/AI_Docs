import streamlit as st
import pandas as pd
import joblib

# Load model
@st.cache_data
def load_model():
    with open('kidney_disease_model', 'rb') as file:
        loaded_model = joblib.load(file)
    return loaded_model

loaded_model = load_model()

# Category map for encoding categorical features
category_map = {
    'red_blood_cells': {'normal': 0, 'abnormal': 1},
    'pus_cell': {'normal': 0, 'abnormal': 1},
    'pus_cell_clumps': {'notpresent': 0, 'present': 1},
    'bacteria': {'notpresent': 0, 'present': 1},
    'hypertension': {'no': 0, 'yes': 1},
    'diabetes_mellitus': {'no': 0, 'yes': 1},
    'coronary_artery_disease': {'no': 0, 'yes': 1},
    'appetite': {'poor': 0, 'good': 1},
    'pedal_edema': {'no': 0, 'yes': 1},
    'anemia': {'no': 0, 'yes': 1}
}

# Create input dataframe
def create_input_df(user_inputs, category_map):
    for category in category_map:
        if category in user_inputs:
            user_inputs[category] = category_map[category].get(user_inputs[category], -1)
    input_df = pd.DataFrame([user_inputs])
    return input_df

# Sidebar navigation
st.sidebar.title('Prediction')
options = st.sidebar.selectbox('Select a page:', ['Prediction'])

if options == 'Prediction':
    st.title('🩺 Chronic Kidney Disease Prediction')
    st.markdown("### Enter Patient Details:")

    # Categorical Inputs
    red_blood_cells = st.radio('Red Blood Cells', ('normal', 'abnormal'))
    pus_cell = st.radio('Pus Cell', ('normal', 'abnormal'))
    pus_cell_clumps = st.radio('Pus Cell Clumps', ('notpresent', 'present'))
    bacteria = st.radio('Bacteria', ('notpresent', 'present'))
    hypertension = st.radio('Hypertension', ('no', 'yes'))
    diabetes_mellitus = st.radio('Diabetes Mellitus', ('no', 'yes'))
    coronary_artery_disease = st.radio('Coronary Artery Disease', ('no', 'yes'))
    appetite = st.radio('Appetite', ('poor', 'good'))
    pedal_edema = st.radio('Pedal Edema', ('no', 'yes'))
    anemia = st.radio('Anemia', ('no', 'yes'))

    # Numerical Inputs
    age = st.slider('Age', 0, 100, 0)
    blood_pressure = st.slider('Blood Pressure', 0, 180, 0)
    specific_gravity = st.slider('Specific Gravity', 0.0, 2.0, 0.0)
    albumin = st.slider('Albumin', 0, 5, 0)
    sugar = st.slider('Sugar', 0, 5, 0)
    blood_glucose_random = st.slider('Blood Glucose Random', 0, 500, 0)
    blood_urea = st.slider('Blood Urea', 0, 200, 0)
    serum_creatinine = st.slider('Serum Creatinine', 0.0, 10.0, 0.0)
    sodium = st.slider('Sodium', 0, 200, 0)
    potassium = st.slider('Potassium', 0, 10, 0)
    hemoglobin = st.slider('Hemoglobin', 0, 20, 0)
    packed_cell_volume = st.slider('Packed Cell Volume', 0, 100, 0)
    white_blood_cell_count = st.slider('White Blood Cell Count', 0, 20000, 0)
    red_blood_cell_count = st.slider('Red Blood Cell Count', 0, 10, 0)

    user_inputs = {
        'age': age,
        'blood_pressure': blood_pressure,
        'specific_gravity': specific_gravity,
        'albumin': albumin,
        'sugar': sugar,
        'red_blood_cells': red_blood_cells,
        'pus_cell': pus_cell,
        'pus_cell_clumps': pus_cell_clumps,
        'bacteria': bacteria,
        'blood_glucose_random': blood_glucose_random,
        'blood_urea': blood_urea,
        'serum_creatinine': serum_creatinine,
        'sodium': sodium,
        'potassium': potassium,
        'hemoglobin': hemoglobin,
        'packed_cell_volume': packed_cell_volume,
        'white_blood_cell_count': white_blood_cell_count,
        'red_blood_cell_count': red_blood_cell_count,
        'hypertension': hypertension,
        'diabetes_mellitus': diabetes_mellitus,
        'coronary_artery_disease': coronary_artery_disease,
        'appetite': appetite,
        'pedal_edema': pedal_edema,
        'anemia': anemia
    }

    if st.button('Predict'):
        input_df = create_input_df(user_inputs, category_map)
        prediction = loaded_model.predict(input_df)[0]

        st.markdown("---")
        st.markdown("### 🧾 Prediction Result:")

        if prediction == 0:
            st.error("**High Risk:** The patient is likely to have Chronic Kidney Disease. Immediate medical attention is advised.")
        elif prediction == 1:
            st.warning("**Moderate Risk:** Some symptoms may indicate early signs. Please consult a doctor for further evaluation.")
        else:
            st.success("**Low Risk:** The patient is unlikely to have Chronic Kidney Disease. Keep maintaining a healthy lifestyle.")

        st.markdown("---")
