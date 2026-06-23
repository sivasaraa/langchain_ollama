import os
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
import wikipedia

wikipedia.set_user_agent("MyLangChainBot/1.0 (contact: your_email@example.com)")

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)
wikipedia_tool = WikipediaQueryRun(api_wrapper=api_wrapper)

print("Tool Name:", wikipedia_tool.name)
print("Tool Description:", wikipedia_tool.description)

query_result = wikipedia_tool.run("Artificial Intelligence")
print(query_result)

def main():
    print("Hello from wikipedia-tool!")


if __name__ == "__main__":
    main()
