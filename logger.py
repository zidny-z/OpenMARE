import logging
from datetime import datetime
from pathlib import Path


def setup_logger():
	Path("logs").mkdir(exist_ok=True)

	run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
	log_path = f"logs/run_{run_id}.log"

	logging.basicConfig(
		level=logging.INFO,
		format="%(asctime)s | %(levelname)s | %(message)s",
		handlers=[logging.FileHandler(log_path), logging.StreamHandler()],
	)

	logging.info("OpenMARE run started")
	return run_id
