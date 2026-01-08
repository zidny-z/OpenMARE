from langchain_core.prompts import ChatPromptTemplate

from prompt_loader import load_prompt


def srs_chain(llm):
	prompt = ChatPromptTemplate.from_messages(
		[
			("system", load_prompt("srs_writer")),
			("human", "{requirements}"),
		]
	)
	return prompt | llm
