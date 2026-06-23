from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import wikipedia   

import wikipedia_tool

# 1. Fix user-agent connection
wikipedia.set_user_agent("MyLangChainBot/1.0 (contact: your_email@example.com)")

# 2. Build the actual tool object
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

model = ChatOllama(model="llama3.2", temperature=0)
tools = [wikipedia_tool]

agent = create_agent(model=model, tools=tools,
                     system_prompt='You are a helpful assistant. Use the Wikipedia tool to verify facts before answering questions.')

response = agent.invoke({
        "messages": [{"role": "user", "content": "What is the capital of France according to Wikipedia?"}]
    })

print(response)