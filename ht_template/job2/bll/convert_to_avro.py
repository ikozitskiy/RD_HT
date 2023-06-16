from typing import List, Dict, Any
from fastavro import json_reader


def convert_to_avro(path: str):
    file_location_from = path + '/' + path.split('/')[-1] + '.json'
    with open(file_location_from,'r') as f:
        data = f.read()
    return data

