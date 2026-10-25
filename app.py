import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from textblob import TextBlob
from dotenv import load_dotenv
import os
import warnings

warnings.filterwarnings("ignore")

load_dotenv()
API_KEY = os.getenv('NEWS_API_KEY')

st.set_page_config(
    page_title="News Sentiment Analysis Dashboard",
    layout="wide"
)

st.title("News Sentiment Analysis Dashboard")
st.markdown(
    '''
Track real-time sentiment of global news headlines using Python and NewsAPI 
    '''
)

default_topics = ['Artificial Intelligence', 'OpenAI', 'NVIDIA', 'Google Gemini', 'Claude', 'Cyber Security']

if 'topics' not in st.session_state:
    st.session_state.topics = default_topics

st.sidebar.header("Dashboard Controls")

new_topic = st.sidebar.text_input('Add a new topic')

if st.sidebar.button("Add New Topic"):
    if new_topic and new_topic not in st.session_state.topics:

        st.session_state.topics.append(new_topic)

selected_topic = st.sidebar.selectbox('Choose Topic',
                                      st.session_state.topics)

article_limit = st.sidebar.slider('Number of Articles to Display', 5, 20, 15)

url = (
    f'https://newsapi.org/v2/everything?'
    f'q={selected_topic}&'
    f'pageSize={article_limit}&'
    f'sortBy=publishedAt&'
    f'language=en&'
    f'apiKey={API_KEY}'
)

response = requests.get(url)
data = response.json()

articles = data.get("articles", [])

news_data = []
for article in articles:
    title = article['title']

    analysis = TextBlob(title)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    news_data.append({
        'Title': title,
        'Source': article['source']['name'],
        'PublishedAt': article['publishedAt'][:10],
        'Polarity': polarity,
        'Sentiment': sentiment,
        "url": article["url"]
    })

df = pd.DataFrame(news_data)

positive_count = len(df[df['Sentiment'] == 'Positive'])
negative_count = len(df[df['Sentiment'] == 'Negative'])
neutral_count = len(df[df['Sentiment'] == 'Neutral'])

col1, col2, col3 = st.columns(3)

col1.metric('Positive', positive_count)
col2.metric('Neutral', neutral_count)
col3.metric('Negative', negative_count)

fig = px.pie(df, names='Sentiment', title=f'Sentiment Distribution for {selected_topic}')

st.plotly_chart(fig, use_container_width=True)

hist_fig = px.histogram(df, x='Polarity', color='Sentiment', title='Headline Polarity Distribution')
st.plotly_chart(hist_fig, use_container_width=True)

st.subheader('Latest Headlines')

for index, row in df.iterrows():
    st.markdown(row['Title'], unsafe_allow_html=True)
    st.write(f"Source: {row['Source']}")
    st.write(f"Published At: {row['PublishedAt']}")
    st.write(f"Sentiment: {row['Sentiment']}")

    st.markdown(f"[Read Full Article]({row['url']})")
    st.markdown(f'---')
