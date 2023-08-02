import os
import streamlit as sl
from apikey import apikey

os.environ['OPENAI_API_KEY'] = apikey
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.memory import ConversationBufferMemory

#App framework 
sl.title('Ways to save Earth 🌎')
prompt = sl.text_input("Ask me:")

#Prompt templates
tips_template = PromptTemplate(
  input_variables=['topic'],   
  template="I want a response in the following ruleset: (Topic=[{topic}]; Format =[ One paragraph starting with one tip about the topic for improving the world in the subject of (topic), how I can work to achieve the improvement and how the world is gonna be improved by doing so] ; Language= [The topic language] )"                                           
)

goals_template = PromptTemplate(
  input_variables=['tip'],   
  template="I want a response in the following ruleset: (Tip=[{tip}]; Format =[ Find the united nation's sustainable development goal that fits best with the tip and write it as (Goal X: Goal name)] ; Language= [The tip language] )"                                                       
)

#Memory
memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')


#LLM - definição da LLM usada
llm= OpenAI (temperature=0.9) #Diz quão criativo será nosso modelo
tips_chain = LLMChain (llm=llm, prompt=tips_template, verbose= True, output_key='tip')
goals_chain = LLMChain (llm=llm, prompt=goals_template, verbose= True, output_key='goal')
sequential_chain= SequentialChain(chains=[tips_chain, goals_chain],input_variables=['topic'],output_variables=['tip','goal'], verbose=True)

if prompt: #Função que passa o prompt para a LLM
  response = sequential_chain({'topic': prompt})
  sl.write(response['tip'])
  sl.write(response['goal']) #Mo#Mostra a resposta da LLM  
  with sl.expander('Message History'):
    sl.info(memory.buffer)