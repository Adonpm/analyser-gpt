import asyncio
from teams.analyser_gpt import getDataAnalyserTeam
from models.openai_model_client import get_model_client
from config.docker_util import getDockerCommandLineExecutor, start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage

async def main():
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    team = getDataAnalyserTeam(docker, openai_model_client)

    try:
        task = "Can you give me a graph of types of flowers in my data iris.csv"
        await start_docker_container()
        async for message in team.run_stream(task=task):
            print(message)

    except Exception as e:
        print("Error occured: ", e)

    finally:
        await stop_docker_container()

if __name__ == "__main":
    asyncio.run(main())
