'''
Ogi Hadicahyo

Objective: Creating a page for NLP Exploratory Data Analysis
'''

import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

def run():
    '''
    Function for EDA page
    '''
    st.title('Exploration Data Analysis Section')
# ============================= Showing Data ==========================
    df = pd.read_csv('eda.csv')
    horizontal_radio_css = """<style>div.row-widget.stRadio > div{flex-direction:row;}</style>"""
    st.markdown(horizontal_radio_css, unsafe_allow_html=True)
    data_show = st.radio("**Viewing Options**", ['Top 10 Entries', 'Bottom 10 Entries'])
    if data_show == 'Top 10 Entries':
        st.table(df.head(10))
    else:
        st.table(df.tail(10))
# ============================= Simple Analysis ========================

    # Sentiment Distribution
    st.header('1. Sentiment Distribution')
    image = Image.open('Sentiment_Distribution.png')
    st.image(image, caption='Figure 1:Sentiment Distribution')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            **The largest segment is Positive**, which covers **64%** of the distribution with a total of **19,015**. **The next largest** is **Negative Sentiment** which accounts for **21.3%** of the distribution with a total of **6,321**. **The smallest segment** is **Neutral Sentiment**, accounting for **14.7%** of the distribution with a count of **4,356**. From these numbers, we can conclude that most of the sentiment in the dataset is positive, indicating that most of the responses, reviews, or comments collected express positive feelings. **Positive sentiment was more common than negative sentiment**, indicating that the sample generally had better or optimistic sentiment.
            ''')
    st.markdown('---')

    # Sentiment Polarity Distribution
    st.header('2. Sentiment Polarity Distribution')
    image = Image.open('Sentiment_Polarity_Distribution.png')
    st.image(image, caption='Figure 2:Sentiment Polarity Distribution')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            - Positive sentiment: The frequency of positive sentiment is higher than negative and neutral sentiment. This shows that overall, the data analyzed has positive sentiment.
            - Negative sentiment: The frequency of negative sentiment is low, indicating that negative sentiment is not dominant in the data.
            - Neutral sentiment: The frequency of neutral sentiment is relatively low, indicating that the data generally has a positive or negative sentiment.

            Image analysis shows that the data analyzed has an overall positive sentiment. Negative and neutral sentiment is low.
            ''')
    st.markdown('---')

    # Sentiment Polarity Distribution
    st.header('3. Sentiment Subjectivity Distribution')
    image = Image.open('Sentiment_Subjectivity_Distribution.png')
    st.image(image, caption='Figure 3: Sentiment Subjectivity Distribution')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            From the observation above, this distribution suggests that a considerable portion of the analyzed sentiments are deemed objective. Subjective sentiments are distributed across the spectrum with a peak in positive sentiments at the higher subjectivity scores. The presence of both neutral and negative sentiments across the subjectivity range indicates a diverse set of opinions and perspectives in the underlying data. The data suggests that while subjective expressions of sentiment are present, they may not dominate the conversation as much as objective statements.
            ''')
    st.markdown('---')

    # Sentiment Polarity Distribution
    st.header('4. Sentiment Polarity vs Sentiment Subjectivity')
    image = Image.open('Sentiment_Polarity_and_Subjectivity_Distribution.png')
    st.image(image, caption='Figure 4: Sentiment Polarity vs Sentiment Subjectivity')
    with st.expander("**Insight From The Visualization**"):
        st.write(
            '''
            Based on the scatter plot analysis, it can be concluded that the data generally has positive and subjective sentiment. There is some data that has positive and objective sentiment, and there is also data that has negative sentiment.
            ''')
    st.markdown('---')
    
# ============================= Positive Word Cloud ==================================
    st.subheader('Positive Sentiment Word Cloud')
    image1 = Image.open('positive_wordcloud.png')
    st.image(image1, caption='Figure 5 Positive Sentiment Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Positive word cloud offers an insightful visualization of commonly used words associated with positive sentiment, featuring terms like **good, game, love, great, like, and time.** These words are frequently employed when individuals express positive sentiments in their reviews or feedback. The prevalence of these terms in the word cloud signifies their significance in describing positive experiences or aspects of products/services. 
            '''
            )

# ============================= Negative Word Cloud =====================================

    st.subheader('Negative Sentiment Word Cloud')
    image2 = Image.open('negative_wordcloud.png')
    st.image(image2, caption='Figure 6 Negative Sentiment Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Negative word cloud provides a visual representation of commonly used words associated with negative sentiment, including **game, time, get, nt, s, and like.** These terms are frequently expressed when individuals convey negative sentiments in their reviews or comments. The prominence of these words in the word cloud suggests that they are often used to describe aspects of experiences or products that are perceived negatively. 
            '''
            )

# =============================== Neutral Word Cloud ====================================

    st.subheader('Neutral Sentiment Word Cloud')
    image3 = Image.open('neutral_wordcloud.png')
    st.image(image3, caption='Figure 7 Neutral Sentiment Word Cloud',  width=700)

    # explaination
    with st.expander('Explanation'):
        st.caption(
            '''
            The Neutral word cloud highlights commonly used words related to neutral sentiment, such as **nt, work, like, ca, time, and please**. These terms are frequently expressed when people describe neutral sentiments, suggesting that they are often used in reviews or comments that convey neither particularly positive nor negative feelings. This word cloud provides insight into the language commonly associated with neutral sentiments in the analyzed dataset.
            '''
            )
if __name__== '__main__':
    run()