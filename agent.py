from langchain_openai import ChatOpenAI
import os
from petshop import SearchProductsByDescription
from langchain.agents import Tool, create_react_agent
from langchain import hub

class AgentOpenAiFunctions:

    def __init__(self):

        llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
        products_by_description = SearchProductsByDescription()

        self.tools = [
            Tool(
                name = products_by_description.name,
                func = products_by_description.run,
                description = products_by_description.description
            )
        ]

        prompt = hub.pull("hwchase17/react")
        self.agent = create_react_agent(llm, self.tools, prompt)