from typing import List, Dict, Any
import os

from ht_template.job2.bll.convert_to_avro import convert_to_avro


def rewrite_to_dir(json_dir: str, avro_dir: str) -> None:
    exact_avro_path = avro_dir + '/' + avro_dir.split('/')[-1] + '.avro'
    if not os.path.exists(avro_dir):
        os.makedirs(avro_dir)
    for files in os.listdir(avro_dir):
        os.remove(avro_dir + '/' + files)
    with open(exact_avro_path, 'w') as file:
        file.write(convert_to_avro(json_dir))
