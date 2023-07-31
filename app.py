import os
import streamlit as sl
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

#App framework 
sl.title('Ways to save Earth 🌎')
prompt = sl.text_input("Ask me:")

#Prompt templates
tips_template = PromptTemplate(
  input_variables=['topic'],   
  template='Write me one tip of how to save Earth in the field of: {topic}'                        
                                
)

#LLM - definição da LLM usada
llm= OpenAI (temperature=0.9) #Diz quão criativo será nosso modelo
tips_chain = LLMChain (llm=llm, prompt=tips_template, verbose= True)

if prompt: #Função que passa o prompt para a LLM
  response = tips_chain.run(prompt)
  sl.write(response) #Mostra a resposta da LLM