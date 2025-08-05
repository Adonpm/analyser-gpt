from autogen_agentchat.agents import AssistantAgent
from prompts.data_analyser_message import DATA_ANALYSER_SYSTEM_MESSAGE

def getDataAnalyserAgent(model_client):
    data_analyser_agent = AssistantAgent(
        name="Data_Analyser_Agent",
        model_client=model_client,
        description="An agent that solves data analysis problems and gives the code as well.",
        system_message=DATA_ANALYSER_SYSTEM_MESSAGE
    )
    return data_analyser_agent