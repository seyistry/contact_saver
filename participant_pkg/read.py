import file_ops
from pathlib import Path
workspace = Path("workspace")

csv_file = workspace / "contact.csv"
file_ops.load_participants(csv_file)