import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model='llama3.2', temperature=0.7, num_predict=128)
def restaurantName(cuisine):
    prompt = ChatPromptTemplate.from_template('suggest one restaurant name for {cuisine} cuisine')
    chain = prompt | model | StrOutputParser()
    restaurant_name = chain.invoke({'cuisine': cuisine})
    print(restaurant_name)
    return restaurant_name

st.title('Restaurant Name Selector')
cuisine = st.sidebar.selectbox('Select Cuisine', ['Indian', 'Italian', 'Arab', 'Continental', 'Asian'])

if cuisine:
    response = restaurantName(cuisine)
    st.write(response)



