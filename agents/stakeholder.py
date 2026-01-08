from langchain_core.prompts import ChatPromptTemplate

from prompt_loader import load_prompt


def stakeholder_chain(llm):
	prompt = ChatPromptTemplate.from_messages(
		[
			("system", load_prompt("stakeholder")),
			("human", "{idea}"),
		]
	)
	return prompt | llm
