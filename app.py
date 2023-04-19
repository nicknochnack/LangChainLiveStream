# import streamlit for the app 
import streamlit as st

# Import langchain stuff 
from langchain.agents import load_tools, initialize_agent, AgentType
from langchain.llms import OpenAI

# Import apikey and set it to the environment
import os 
from apikey import apikey

# Set the apikey
os.environ['OPENAI_API_KEY'] = apikey

# Initializing the LLM and the Toolset
llm = OpenAI(temperature=0)
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

st.title('Wikipedia Langchain Bot 🦜')
# Collect the prompt from the user 
input = st.text_input('Type Your Prompt Here')

if input: 
    text = agent.run(input)
    st.write(text)