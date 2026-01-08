from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def get_llm():
	return ChatOpenAI(model="deepseek-chat", temperature=0)
