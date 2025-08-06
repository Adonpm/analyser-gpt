from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from agents.code_executor_agent import getCodeExecutorAgent
from agents.data_analyser_agent import getDataAnalyserAgent

def getDataAnalyserTeam(docker, model_client):
    code_executor_agent = getCodeExecutorAgent(docker)
    data_analyser_agent = getDataAnalyserAgent(model_client)

    text_mention_termination = TextMentionTermination("STOP")

    team = RoundRobinGroupChat(
        participants=[data_analyser_agent, code_executor_agent],
        termination_condition=text_mention_termination,
        max_turns=10
    )

    return team
