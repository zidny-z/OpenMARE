from langchain_core.prompts import ChatPromptTemplate

from prompt_loader import load_prompt


def checker_chain(llm):
	prompt = ChatPromptTemplate.from_messages(
		[
			("system", load_prompt("checker")),
			("human", "{srs}"),
		]
	)
	return prompt | llm
