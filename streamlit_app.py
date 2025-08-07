import streamlit as st
import asyncio
import os
from teams.analyser_gpt import getDataAnalyserTeam
from models.openai_model_client import get_model_client
from config.docker_util import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

st.title("Analyser GPT - Your AI Data Analyst")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

task = st.chat_input("Enter your task here")

# For showcasing chat history within UI
if "messages" not in st.session_state:
    st.session_state.messages = []

# For providing state to autogen team
if "autogen_team_state" not in st.session_state:
    st.session_state.autogen_team_state = None

# To only dispaly "output.png" if it was not there in state
if "images_shown" not in st.session_state:
    st.session_state.images_shown = []

async def run_analyzer_gpt(docker, model_client, task):
    try:
        await start_docker_container(docker)
        team = getDataAnalyserTeam(docker, model_client)

        # For providing state to autogen team
        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)


        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                if message.source == "user":
                    with st.chat_message('user', avatar="👤"):
                        st.markdown(message.content)
                if message.source == "Python_Code_Executor_Agent":
                    with st.chat_message("Python Code Executor", avatar="👩‍💻"):
                        st.markdown(message.content)
                if message.source == "Data_Analyser_Agent":
                    with st.chat_message("Data Analyser Agent", avatar="🧑‍🔬"):
                        st.markdown(message.content)

                st.session_state.messages.append(message.content)

            if isinstance(message, TaskResult):
                st.markdown(f"Stop Reason: {message.stop_reason}")

                st.session_state.messages.append(message.stop_reason)
        
        # Saving state 
        st.session_state.autogen_team_state = await team.save_state()
        return None

    except Exception as e:
        st.error(f"Error: {e}")
        return e

    finally:
        await stop_docker_container(docker)

# For showcasing chat history within UI
if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)

if task:
    if uploaded_file is not None:

        os.makedirs("temp", exist_ok=True)
        with open("temp/data.csv", "wb") as f:
            f.write(uploaded_file.getbuffer())

        model_client = get_model_client()
        docker = getDockerCommandLineExecutor()

        asyncio.run(run_analyzer_gpt(docker, model_client, task))

        if os.path.exists("temp/output.png"):
            if "temp/output.png" not in st.session_state.images_shown:
                st.session_state.images_shown.append("temp/output.png")
                st.image("temp/output.png", caption="Output Image", use_container_width=True)

    else:
        st.warning("Please upload the file")

else:
    st.warning("Please provide the task")