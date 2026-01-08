from dataclasses import dataclass, field
from typing import List


@dataclass
class Workspace:
	idea: str = ""
	stakeholder_needs: str = ""
	requirements: str = ""
	srs: str = ""
	issues: List[str] = field(default_factory=list)
