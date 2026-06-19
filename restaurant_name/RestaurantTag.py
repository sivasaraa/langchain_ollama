import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(model='llama3.2', temperature=0.5, num_predict=256)

def restaurantMenu(cuisine):
    prompt1 = ChatPromptTemplate.from_template('suggest a company name for the {cuisine} cuisine')
    chain1 = prompt1 | model | StrOutputParser()

    prompt2 = ChatPromptTemplate.from_template('suggest a tag line for the {restaurant}')
    chain2 = prompt2 | model | StrOutputParser()

    fullchain = {'restaurant' : chain1} | chain2
    response = fullchain.invoke({'cuisine': cuisine})
    print(response)
    return response


st.title('Restaurant TagLine Generator')
cuisine = st.sidebar.selectbox('cuisine' , ['Indian', 'American', 'Italian', 'Japanese'])
if cuisine:
    response = restaurantMenu(cuisine)
    st.write(response)
