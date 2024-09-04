from tools import terminal_tool,save_tool,search_tool,weather_tool
from src.agent.react import ReactAgent
from src.inference.groq import ChatGroq
from os import environ
from dotenv import load_dotenv
from experimental import *

load_dotenv()
api_key=environ.get('GROQ_API_KEY')
llm=ChatGroq('llama-3.1-70b-versatile',api_key,temperature=0)

input=input("Enter a query: ")
tools=[weather_tool]
instructions=[]
agent=ReactAgent(name='AI Agent',description='You are a helpful AI Assistant',instructions=instructions,tools=tools,llm=llm,verbose=True)
response=agent.invoke(input)
print(response)

# responses=agent.stream(input)
# for response in responses:
#     print(response)