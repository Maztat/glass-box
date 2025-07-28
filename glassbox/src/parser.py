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

def get_valid_files(requested_files: list[str], config_path: str=".glassbox") -> dict[str,str]:
    """Returns only files from requested_files that are also allowed in the config file."""
    config_valid = get_files(config_path)
    valid = {}

    for file in requested_files:
        if file in config_valid:
            valid[file] = config_valid[file]

    return valid