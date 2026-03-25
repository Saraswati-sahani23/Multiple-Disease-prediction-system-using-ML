# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:41:58 2026

@author: saras
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

parkinson_model = pickle.load(open('C:/Users/saras/Desktop/Machinelearning/Multiple disease prediction system/models/parkinson_model (5).sav','rb'))

heart_model = pickle.load(open('C:/Users/saras/Desktop/Machinelearning/Multiple disease prediction system/models/heart_model.sav','rb'))
diabetes_model = pickle.load(open('C:/Users/saras/Desktop/Machinelearning/Multiple disease prediction system/models/trained_model.sav','rb'))

breastcancer_model = pickle.load(open('C:/Users/saras/Desktop/Machinelearning/Multiple disease prediction system/models/breast-cancer.sav','rb'))

with st.sidebar:
    selected = option_menu('Multiple disease prediction system',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinson Prediction',
                            'Breast Cancer Prediction'],
                           icons = ['activity','heart','person','file-medical'],
                             default_index = 0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ml')
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood pressure value')
    SkinThickness = st.text_input('Skin thickness value')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction value')
    Age = st.text_input('Age of the person')
    
    diagnosis = ''
    
    
    if st.button('Diabetes result'):
        prediction = diabetes_model.predict([[
           Pregnancies,Glucose, BloodPressure, SkinThickness, 
            Insulin, BMI, DiabetesPedigreeFunction, Age
        ]])
        
        if prediction[0] == 1:
            diagnosis = "The person is not diabetic"
        else:
            diagnosis = "The person is diabetic"
        
        st.success(diagnosis)

    
       
if(selected == 'Heart Disease Prediction'):
       st.title('Heart Disease prediction using ml')
    
       Age = st.text_input('Age of the person')
       Sex = st.text_input('Sex (0 = female, 1 = male)')
       ChestPainType = st.text_input('Chest pain type (0-3)')
       BP = st.text_input('Resting blood pressure')
       Cholesterol = st.text_input('Serum cholesterol in mg/dl')
       FBS = st.text_input('Fasting blood sugar > 120 mg/dl (0 = no, 1 = yes)')
       EKG = st.text_input('Resting electrocardiographic results (0-2)')
       MaxHR = st.text_input('Maximum heart rate achieved')
       ExerciseAngina = st.text_input('Exercise induced angina (0 = no, 1 = yes)')
       STDepression = st.text_input('ST depression induced by exercise')
       SlopeST = st.text_input('Slope of peak exercise ST segment (0-2)')
       NumVessels = st.text_input('Number of major vessels colored by fluoroscopy (0-3)')
       Thallium = st.text_input('Thallium stress test (1-3)')
    
       diagnosis = ''
    
       if st.button('Heart Disease result'):
           prediction = heart_model.predict([[
               Age, Sex, ChestPainType, BP, Cholesterol, FBS, 
               EKG, MaxHR, ExerciseAngina, STDepression, SlopeST, NumVessels, Thallium
           ]])
        
           if prediction[0] == 1:
               diagnosis = "The person has heart disease"
           else:
               diagnosis = "The person does not have heart disease"
           
           st.success(diagnosis)
       
if selected == 'Parkinson Prediction':
    st.title("Parkinson Disease Prediction using ML")

    Age = st.text_input('Age')
    Tremor_Intensity = st.text_input('Tremor Intensity')
    Voice_Pitch = st.text_input('Voice Pitch')
    Voice_Jitter = st.text_input('Voice Jitter')
    Voice_Shimmer = st.text_input('Voice Shimmer')
    Bradykinesia_Score = st.text_input('Bradykinesia Score')
    Postural_Instability = st.text_input('Postural Instability')
    Rigidity_Level = st.text_input('Rigidity Level')
    UPDRS_Score = st.text_input('UPDRS Score')
    Handwriting_Change = st.text_input('Handwriting Change')
    Walking_Difficult = st.text_input('Walking Difficulty')
    MRI_Score = st.text_input('MRI Score')

    diagnosis = ''

    if st.button('Parkinson Result'):
        prediction = parkinson_model.predict([[
            Age, Tremor_Intensity, Voice_Pitch, Voice_Jitter,
            Voice_Shimmer, Bradykinesia_Score, Postural_Instability,
            Rigidity_Level, UPDRS_Score, Handwriting_Change,
            Walking_Difficult, MRI_Score
        ]])

        if prediction[0] == 1:
            diagnosis = "The person has Parkinson's disease"
        else:
            diagnosis = "The person does not have Parkinson's disease"

        st.success(diagnosis)
        
        
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')

    radius_mean = st.text_input('Radius Mean')
    texture_mean = st.text_input('Texture Mean')
    perimeter_mean = st.text_input('Perimeter Mean')
    area_mean = st.text_input('Area Mean')
    smoothness_mean = st.text_input('Smoothness Mean')
    compactness_mean = st.text_input('Compactness Mean')
    concavity_mean = st.text_input('Concavity Mean')
    concave_points_mean = st.text_input('Concave Points Mean')
    symmetry_mean = st.text_input('Symmetry Mean')
    fractal_dimension_mean = st.text_input('Fractal Dimension Mean')

    radius_worst = st.text_input('Radius Worst')
    texture_worst = st.text_input('Texture Worst')
    perimeter_worst = st.text_input('Perimeter Worst')
    area_worst = st.text_input('Area Worst')
    smoothness_worst = st.text_input('Smoothness Worst')
    compactness_worst = st.text_input('Compactness Worst')
    concavity_worst = st.text_input('Concavity Worst')
    concave_points_worst = st.text_input('Concave Points Worst')
    symmetry_worst = st.text_input('Symmetry Worst')
    fractal_dimension_worst = st.text_input('Fractal Dimension Worst')

    diagnosis = ''

    if st.button('Breast Cancer Result'):
        prediction = breastcancer_model.predict([[
            radius_mean, texture_mean, perimeter_mean, area_mean,
            smoothness_mean, compactness_mean, concavity_mean,
            concave_points_mean, symmetry_mean, fractal_dimension_mean,
            radius_worst, texture_worst, perimeter_worst, area_worst,
            smoothness_worst, compactness_worst, concavity_worst,
            concave_points_worst, symmetry_worst, fractal_dimension_worst
        ]])

        if prediction[0] == 1:
            diagnosis = "The tumor is malignant (cancerous)"
        else:
            diagnosis = "The tumor is benign (non-cancerous)"

        st.success(diagnosis)