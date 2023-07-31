import os
import streamlit as sl
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate


#App framwork 
sl.title('Ways to save Earth 🌎')
prompt = sl.text_input("Ask me:")

#Prompt templates
title_template = PromptTemplate(
  input_variables=['topic'],   
  template='write me one way to save earth about: {topic}'                        
                                
)

#LLM - definição da LLM usada
llm= OpenAI (temperature=0.9) #Diz quão criativo será nosso modelo

if prompt: #Função que passa o prompt para a LLM
  response = llm(prompt)
  sl.write(response) #Mostra a resposta da LLM