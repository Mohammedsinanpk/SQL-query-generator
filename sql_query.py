import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
import os
gpt_api_key = os.environ.get('GPT_API_key')

st.title("SQL query searcher")
sql_query= st.text_input("Generate SQL query to...")
button = st.button("search")

PREFIX = "You are a sql query chatbot, Only give answer to sql related queries, If asked anything else, ask to ask sql related query.You can have access to the following tools"

llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=gpt_api_key)
tools = load_tools(["wikipedia"], llm=llm)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, agent_kwargs={'prefix':PREFIX})
if button:
    response=agent.invoke(sql_query)
    st.text(response['output'])
