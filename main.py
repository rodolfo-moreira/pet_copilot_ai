import streamlit as st
from agent import AgentOpenAiFunctions
from langchain.agents import AgentExecutor
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Petshop Copilot AI", layout="wide")
st.title("Petshop Copilot AI")
st.write("Get Tailored advice and top recommendations from our specialists-just talk!")

question = st.text_input("Ask your question:")

if st.button("Search"):
    with st.spinner("Searching...."):
        agent = AgentOpenAiFunctions()
        executor = AgentExecutor(
            agent=agent.agent,
            tools=agent.tools,
            verbose=True,
            hangdle_parsing_errors=True
        )

        answer = executor.invoke({"input": question})
        print(answer["output"])
    
    st.subheader("Agent Answer")
    st.write(answer["output"])