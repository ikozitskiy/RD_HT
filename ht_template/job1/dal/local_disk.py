from typing import List, Dict, Any
import os


def save_to_disk(json_content: List[Dict[str, Any]], path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path)
    for files in os.listdir(path):
        os.remove(path + '/' + files)
    new_path = path + '/' + (path.split('/'))[-1] + '.json'
    with open(new_path, 'w') as file:
        file.write(str(json_content))
