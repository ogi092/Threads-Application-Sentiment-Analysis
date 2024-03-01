'''
Ogi Hadicahyo

Objective : Creating a main page of the webapps.
'''

import streamlit as st
import eda
import model

# navigating pages
page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Sentiment Classification'])

if page == 'Home Page':
    st.header('Home Page') 
    st.write('')
    st.write('Name  : Ogi Hadicahyo')
    st.markdown('Dataset    : [Play Store Apps Dataset](https://www.kaggle.com/datasets/whenamancodes/play-store-apps/data)')
    st.write("Objective : Developing a Natural Language Processing (NLP) model that can predict user sentiment from app text reviews on the Google Play Store. With this model, the goal is to provide app developers with valuable tools to automatically analyze and understand user sentiment towards their apps. By accurately predicting user sentiment, developers can gain insight into user preferences and concerns, allowing them to improve app features, address issues, and increase overall user satisfaction.")
    st.write('')
    st.caption('Please pick the options in the Select Page Box located on the left of the screen to start!')
    st.write('')
    st.write('')
    
#============================= Background Info ==========================
    
    with st.expander("Background Information"):
        st.caption("The dataset is obtained from keggle. It has this dataset has **64295 entries** with **5 columns**. The columns consist of text reviews from application users who provide positive, negative, or neutral ratings or sentiments towards the applications they use.")
        
#============================= Work Flow ================================
    
    with st.expander("Work Flow"):
        st.caption(
        '''
            - Data loading from keggle
            - Basic Analysis
            - EDA on most common words
            - Text processing in feature engineering
            - Vectorization
            - Building the models
            - Tuning the models
            - Inference
            - Deployment
        '''
        )

#============================= Conclussion =================================
    with st.expander("Conclusion"): # conclusion
        st.caption(
            '''
            We developed a Natural Language Processing (NLP) model to predict user sentiment from text reviews of apps in the Google Play Store. This model will help app developers analyze and understand user sentiment automatically. We will use two models, namely Long Short-Term Memory (LSTM) and conventional RNN models, to analyze the sentiment of app reviews on the Google Play Store.

            Although RNN is slightly better in terms of loss on validation and test data, both LSTM and RNN have the same accuracy on all types of data. Therefore, we choose LSTM as the base model to be further improved.

            The updated LSTM model shows significant performance improvements compared to the base LSTM model. With lower loss rates and higher accuracy rates, updated LSTM models have a better ability to produce accurate predictions on data not seen during training. Additionally, the updated LSTM model also shows better signs of avoiding overfitting compared to the baseline model.
            '''
        )

#============================ Other Page ======================================
elif page == 'Exploration Data Analysis':
    eda.run()
else:
    model.run()