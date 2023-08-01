import os
import streamlit as sl
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

#App framework 
sl.title('Ways to save Earth 🌎')
prompt = sl.text_input("Ask me:")

#Prompt templates
tips_template = PromptTemplate(
  input_variables=['topic'],   
  template='Write me one tip of how to save Earth in the field of: {topic}'                                                
)

goals_template = PromptTemplate(
  input_variables=['tip'],   
  template='Write me one of the UN Sustainable Development Goals that: ({tip}) helps achieve'                                                
)


#LLM - definição da LLM usada
llm= OpenAI (temperature=0.9) #Diz quão criativo será nosso modelo
tips_chain = LLMChain (llm=llm, prompt=tips_template, verbose= True, output_key='tip')
goals_chain = LLMChain (llm=llm, prompt=goals_template, verbose= True, output_key='goal')
sequential_chain= SequentialChain(chains=[tips_chain, goals_chain],input_variables=['topic'],output_variables=['tip','goal'], verbose=True)

if prompt: #Função que passa o prompt para a LLM
  response = sequential_chain({'topic': prompt})
  sl.write(response['tip'])
  sl.write(response['goal']) #Mo#Mostra a resposta da LLM  