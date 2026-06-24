import os
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

model = ChatOllama(model='llama3.2', temperature=0.7)

prompt = ChatPromptTemplate.from_messages([
    ("system", "you are helpful assistant"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | model

store = {}

def get_session_history(session_id:str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


runnable_with_memory = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

config = {"configurable": {"session_id": "chat_456"}}

print("----Turn 1------")
response1 = runnable_with_memory.invoke(
    {"input": "who wan last cricket worldcup"},
    config=config
)

print("first response:", response1)

response2 = runnable_with_memory.invoke({"input":"who is legend in last worldcup"},
                                        config=config)

print("second response:", response2)