from ht_template.job1.dal import local_disk, sales_api
import os


def save_sales_to_local_disk(date: str, raw_dir: str) -> None:
    json_data = sales_api.get_sales(date)
    print("\tI'm in get_sales(...) function!")
    local_disk.save_to_disk(json_data,raw_dir)
    print("\tI'm in save_to_disc(...) function!")

