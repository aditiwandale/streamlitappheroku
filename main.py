import pickle
import streamlit as st
import streamlit.components.v1 as components

from streamlit_option_menu import option_menu
import numpy as np



# loading the saved models




# Load models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))
pcos_model = pickle.load(open('pcos_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction','PCOS Prediction'],
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):

    # page title
    st.title('Diabetes Prediction using ML')
    st.image("diabetes.jpg",use_column_width = True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The person is diabetic'
            st.image('diabetes2.jpg', use_column_width=True)
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.image('healthy.jpg',use_column_width=True)

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):

    # page title
    st.title('Heart Disease Prediction using ML')
    st.image('heart.png',use_column_width= True)

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        try:
            # Convert input values to numeric
            age = float(age)
            sex = float(sex)
            cp = float(cp)
            trestbps = float(trestbps)
            chol = float(chol)
            fbs = float(fbs)
            restecg = float(restecg)
            thalach = float(thalach)
            exang = float(exang)
            oldpeak = float(oldpeak)
            slope = float(slope)
            ca = float(ca)
            thal = float(thal)

            # Make a prediction
            heart_prediction = heart_disease_model.predict(
                [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

            if (heart_prediction[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
                st.image('heart2.jpg', use_column_width=True)
            else:
                heart_diagnosis = 'The person does not have any heart disease'
                st.image('healthy.jpg', use_column_width=True)

        except ValueError:
            st.error('Please enter valid numeric values for all input fields.')

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):

    # page title
    st.title("Parkinson's Disease Prediction using ML")
    st.image('parkinsons.png',use_column_width= True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP,
                                                           Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE,
                                                           DFA, spread1, spread2, D2, PPE]])

        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
            st.image('parkinsons2.jpg',use_column_width=True)
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
            st.image('healthy.jpg',use_column_width=True)
    st.success(parkinsons_diagnosis)

# Diabetes Prediction Page
if (selected == 'PCOS Prediction'):

    # page title
    st.title('PCOS Prediction using ML')
    st.image('pcos3.jpg',use_column_width= True)

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Weight = st.text_input('Weight (in kg)')

    with col3:
        Height = st.text_input('Height (in cm)')

    with col1:
        BloodGroup = st.text_input('Blood Group')

    with col2:
        Cycle = st.text_input('Cycle (R/I)')

    with col3:
        CycleLength = st.text_input('Cycle Length')

    with col1:
        WeightGain = st.text_input('Weight Gain (Y/N)')

    with col2:
        HairGrowth = st.text_input('Hair Growth (Y/N)')

    with col3:
        SkinDark = st.text_input('Skin Darkness (Y/N)')

    with col1:
        HairLoss = st.text_input('Hair Loss (Y/N)')

    with col2:
        Pimples = st.text_input('Pimples (Y/N)')

    with col3:
        FastFood = st.text_input('Do you consume Fast Food on a regular basis?')

    with col1:
        RegEx = st.text_input('Do you exercise regularly?')

    with col2:
        FollL = st.text_input('Left Follicle No.')

    with col3:
        FollR = st.text_input('Right Follicle No.')

    input_data = [
        Age, Weight, Height, BloodGroup, Cycle, CycleLength, WeightGain,
        HairGrowth, SkinDark, HairLoss, Pimples, FastFood, RegEx, FollL, FollR
    ]

    # code for Prediction
    pcos_diagnosis = ''

    # creating a button for Prediction

    if st.button('PCOS Test Result'):
        input_data = np.array(input_data).astype(float)
        pcos_prediction = pcos_model.predict([input_data])

        if (pcos_prediction[0] == 1):
            pcos_diagnosis = 'The person has pcos'
            st.image('pcos2.jpg',use_column_width=True)
        else:
            pcos_diagnosis = 'The person does not have pcos'
            st.image('healthy.jpg',use_column_width=True)

    st.success(pcos_diagnosis)





