import exporter
from llm import get_llm
from logger import setup_logger
from orchestrator import id, run
from workspace import Workspace


def main():
	setup_logger()

	# workspace = Workspace(
	# 	idea="I want to develop a smart home control system that allows homeowners "
	# 	"to monitor and control household devices remotely."
	# )
	workspace = Workspace(
		idea="I want to develop learning management system that allows students "
		"to access course materials, submit assignments, and receive feedback. and dont forget my students are kids"
	)

	llm = get_llm()
	run(workspace, llm)

	print("\n=== FINAL SRS ===\n")
	print(workspace.srs)
	path_file = f"artifacts/{id}/Final_SRS.docx"
	exporter.export_md_to_docx(workspace.srs, path=path_file)


if __name__ == "__main__":
	main()
