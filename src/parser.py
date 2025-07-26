import os
from pathlib import Path


def get_files(config_path=".glassbox") -> dict[str,str]:
    if not os.path.exists(config_path):
        return {}

    files = {}

    with open(config_path) as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                path = Path(line)
                if path.is_file():
                    files[str(path)] = path.read_text()
                elif path.is_dir():
                    for subfile in path.rglob("*"):
                        if subfile.is_file():
                            files[str(subfile)] = subfile.read_text()

    return files