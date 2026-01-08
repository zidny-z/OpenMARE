import logging
from datetime import datetime
from pathlib import Path

from agents.analyst import analyst_chain
from agents.checker import checker_chain
from agents.srs_writer import srs_chain
from agents.stakeholder import stakeholder_chain

id = datetime.now().strftime("%Y%m%d_%H%M%S")


def save_artifact(iteration, name, content):
	# path = Path(f"artifacts/iteration_{iteration}")
	path = Path(f"artifacts/{id}/iteration_{iteration}")
	path.mkdir(parents=True, exist_ok=True)

	file_path = path / f"{name}.txt"
	file_path.write_text(content, encoding="utf-8")

	logging.info(f"Artifact saved: {file_path}")


def run(workspace, llm):
	iteration = 1

	# Initialize chains
	stakeholder = stakeholder_chain(llm)
	analyst = analyst_chain(llm)
	srs_writer = srs_chain(llm)
	checker = checker_chain(llm)

	logging.info("Agent=Stakeholder | Action=ElicitNeeds")
	workspace.stakeholder_needs = stakeholder.invoke({"idea": workspace.idea}).content
	save_artifact(iteration, "stakeholder_needs", workspace.stakeholder_needs)

	logging.info("Agent=BusinessAnalyst | Action=ClarifyRequirements")
	workspace.requirements = analyst.invoke(
		{"stakeholder_needs": workspace.stakeholder_needs}
	).content
	save_artifact(iteration, "requirements", workspace.requirements)

	logging.info("Agent=SRSWriter | Action=WriteSRS")
	workspace.srs = srs_writer.invoke({"requirements": workspace.requirements}).content
	save_artifact(iteration, "srs_draft", workspace.srs)

	logging.info("Agent=Checker | Action=CheckRequirements")
	check_result = checker.invoke({"srs": workspace.srs}).content
	save_artifact(iteration, "checker_report", check_result)

	pass_condition = check_result.strip().upper().startswith("PASS")
	if not pass_condition:
		logging.info("Checker found issues -> refinement triggered")
		iteration += 1

		workspace.requirements += "\n\nIssues raised by checker:\n" + check_result
		save_artifact(iteration, "requirements_refined", workspace.requirements)

		workspace.srs = srs_writer.invoke(
			{"requirements": workspace.requirements}
		).content
		save_artifact(iteration, "srs_final", workspace.srs)

		check_result = checker.invoke({"srs": workspace.srs}).content
		save_artifact(iteration, "checker_report", check_result)

	logging.info("OpenMARE run completed")
	return workspace
