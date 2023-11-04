import streamlit as st
from deta import Deta
import datetime
import streamlit as st
from textblob import TextBlob

def get_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def get_sentiment_emoji(sentiment):
    if sentiment > 0.5:
        return "😃"
    elif sentiment > 0:
        return "🙂"
    elif sentiment < 0:
        return "😔"
    else:
        return "😐"

DATA_KEY='d0fvm2x4qs5_1hQFdbNSpcDasfJ3oo19ERsZxjGzWXxx'
deta=Deta(DATA_KEY)
db=deta.Base('feedback')

def insert_user(email,name,username,feedback,review,rating):
    date_joined=str(datetime.datetime.now())

    return db.put({'key':email,'name':name,'username':username,'feedback':feedback,'review':review,'rating':rating,'date_joined':date_joined})

def fetch_users():
    users=db.fetch()
    return users.items


def star_rating_widget(label, max_stars=5):
    st.write(label)
    stars = st.slider("", 0, max_stars, 0, key=label)
    st.write("Rating:", "⭐" * stars)
def feedbackform():
    email=st.text_input('Enter your email:',placeholder='abc@xyz.com')
    name=st.text_input('Enter your name',placeholder='Enter your Name')
    username=st.text_input('Enter your username: ',placeholder='Enter your name')
    feedback=st.text_area('Feedback',placeholder='Enter your Feedback')
    if feedback:
        sentiment = get_sentiment(feedback)
        emoji = get_sentiment_emoji(sentiment)
        col1,col2=st.columns(2) 
        with col1:   
            st.subheader(f":blue[Sentiment:] {sentiment:.2f}")
        with col2:
            st.subheader(f":blue[Emoji:] {emoji}")
        st.write(":blue[Emoji Slider:]")
        st.slider("Slider", min_value=-1.0, max_value=1.0, value=sentiment, step=0.01, format="%.2f")

    review=st.radio('Good or bad',options=['Good','Bad'])
    rating=st.slider('Enter your rating',min_value=1,max_value=5)
    st.title("Sentiment Slider with Emojis")
    
    submit=st.button('submit')
    if submit:
        insert_user(email,name,username,feedback,review,rating)
    c1,c2,c3,c4=st.columns(4)
    with c1:
        st.write(':blue[Name]',name)
        st.write(':blue[feedback]',feedback)
        st.write(':blue[review]',review)
        st.write(':blue[rating]', "⭐" * rating)






