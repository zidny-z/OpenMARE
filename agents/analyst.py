from langchain_core.prompts import ChatPromptTemplate

from prompt_loader import load_prompt


def analyst_chain(llm):
	prompt = ChatPromptTemplate.from_messages(
		[
			("system", load_prompt("analyst")),
			("human", "{stakeholder_needs}"),
		]
	)
	return prompt | llm
