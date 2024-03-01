'''
Ogi Hadicahyo

Objective : Creating a page for emotion classification
'''
from function import preprocess_text, prediction
import streamlit as st
import pandas as pd
import joblib
import re
from PIL import Image

def run():
    '''
    This function is for running the page for predictions
    '''
    st.subheader("Can you describe what you're going through right now ?")
    user_input = st.text_input(
        label='Express yourself here ↓',
        value='My opinion about this application...',
        max_chars=300,
        key='text_input_key',
        placeholder='Please Type here...',
        disabled=False,
        help='Just express what youre tought'
)
    st.write('')

    st.write('You entered:', user_input)

    # button
    if st.button(label='Identify Your Sentiment'):
        X= preprocess_text(user_input)
        result= prediction([X])
        st.write(result[1])
        if result[0] == 0:
            st.write("Thank you for your positive sentiments! We're glad you enjoyed your experience using our app. We will continue to strive to provide the best service and improve our features for your even better satisfaction.")
        elif result[0] == 1:
            st.write("Sorry for the less than satisfactory experience. We really appreciate your feedback and we will immediately carry out further evaluation to fix the problems you encounter. We hope to provide a better experience in the future.")
        else:
            st.write("Thank you for your feedback. We will continue to work to improve the overall user experience. If you have any further suggestions or questions, please feel free to contact us")