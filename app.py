import streamlit
import joblib
import numpy
import warnings

warnings.filterwarnings('ignore')

models = joblib.load('student_success_models.pkl')

streamlit.title('Student Score Prediction App')

hours_studied = streamlit.number_input('Enter number of study hours', 0.0, 12.0, 1.0)
attendence = streamlit.number_input('Enter number of attendance percentage', 0.0, 100.0, 70.0)
sleep_hours = streamlit.number_input('Enter number of sleep hours', 0.0, 12.0, 6.0)
tutoring_sessions = streamlit.number_input('Enter number of tutoring sessions attended', 0, 20, 5)
physcial_activity = streamlit.number_input('Enter number of physical activity hours', 0.0, 10.0, 1.0)
    
if streamlit.button('Predict Score based on all factors'):
    input_user = numpy.array([[hours_studied, attendence, sleep_hours, tutoring_sessions, physcial_activity]])
    prediction = models.predict(input_user)[0]
    prediction = max(0, min(100, prediction))
    streamlit.success(f'Predicted Score: {prediction:.2f}')  
    
    
if streamlit.button('About section'):
    streamlit.info('This app is created to predict student scores based on various factors using machine learning models.')
    streamlit.info('Developed by Simphiwe Nhlabati')