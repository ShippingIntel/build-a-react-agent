#!/usr/bin/env python3.11

# Standard Library
from functools import wraps
import logging
import os
import requests
from datetime import datetime, timezone

# Langchain
import langchain_core
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.tools import Tool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API Key
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
OPENAI_MODEL = 'gpt-4o-2024-08-06'

# Decorator for error handling
def error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error in {func.__name__}: {str(e)}")
            return {"error": f"{func.__name__} failed. Try another way."}
    return wrapper

# Main agent function
@error_handler
def agent(query: str, openai_model: str):

    # Function to get time zone for a given port name
    def get_time_zone(port_name):
        url = 'https://www.flagshiptechnologies.com/api/get_port_time_zone'
        payload = {'port_name': port_name}
        response = requests.post(url, data=payload)

        if response.status_code == 200:
            return response.json()['gmt_offset']
        else:
            return {'error': f"Error: {response.status_code}, {response.text}"}

    # Tool for getting time zone
    get_time_zone_tool = Tool(
        name="Get Time Zone",
        func=get_time_zone,
        description="Returns time zone when given port name."
    )

    # Function to get the local time
    def get_local_time(port):
        try:
            local_time = datetime.now()
            return local_time.strftime('%Y-%m-%d %H:%M:%S')
        except Exception as e:
            logging.error(f"Error in get_local_time: {str(e)}")
            raise

    # Tool for getting local time
    get_local_time_tool = Tool(
        name="Get Local Time",
        func=get_local_time,
        description="Returns the local time."
    )

    # Initialize the language model
    llm = ChatOpenAI(model_name=openai_model)

    # Template for the initial prompt
    template = f"Pick the best match to current user {query}. User is in San Francisco."
    prompt_template = langchain_core.prompts.PromptTemplate(template=template, input_variables=['query'])

    # List of tools available to the agent
    tools_for_agent = [
        get_time_zone_tool,
        get_local_time_tool
    ]

    # Template for the agent's reasoning process
    react_template = """Answer the following questions as best you can. 

                        You have access to the following tools: {tools}

                        Use the following format:
                        Question: the input question you must answer
                        Thought: you should always think about what to do
                        Action: the action to take, must be one of [{tool_names}]
                        Action Input: the input to the action
                        Observation: the result of the action
                        Thought: I now know the final answer
                        Final Answer: the final answer to the original input question

                        Begin!

                        Question: {input}

                        Thought: {agent_scratchpad}"""

    # Create the prompt template for the agent
    react_prompt = langchain_core.prompts.PromptTemplate(template=react_template,
                                                         input_variables=['agent_scratchpad', 'input', 'tool_names', 'tools'])

    # Create the agent with the language model and tools
    react_agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    # Executor to run the agent
    agent_executor = AgentExecutor(agent=react_agent,
                                   tools=tools_for_agent,
                                   verbose=True,
                                   handle_parsing_errors=True,
                                   max_iterations=10)

    # Format the prompt with the user query
    formatted_prompt = prompt_template.format(query=query)
    result = agent_executor.invoke(input={"input": formatted_prompt}, handle_parsing_errors=True)

    return result.get('output')

# Main entry point
if __name__ == "__main__":
    result = agent('what is current universal time coordinated based on my current time?', OPENAI_MODEL)
    print(result)

# Uncomment the following lines to test another query
# if __name__ == "__main__":
#     result = agent('what is the difference in time zones between Cleveland and San Francisco?', OPENAI_MODEL)
#     print(result)
