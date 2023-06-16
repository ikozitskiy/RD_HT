"""
This file contains the controller that accepts command via HTTP
and trigger business logic layer
"""
import os
from flask import Flask, request
from flask import typing as flask_typing

from ht_template.job2.bll.write_to_dir import rewrite_to_dir



AUTH_TOKEN = os.environ.get("API_AUTH_TOKEN")

if not AUTH_TOKEN:
    print("AUTH_TOKEN environment variable must be set")


app = Flask(__name__)


@app.route('/', methods=['POST'])
def main() -> flask_typing.ResponseReturnValue:
    """
    Controller that accepts command via HTTP and
    trigger business logic layer

    Proposed POST body in JSON:
    {
      "data: "2022-08-09",
      "raw_dir": "/path/to/my_dir/raw/sales/2022-08-09"
    }
    """
    input_data: dict = request.json
    # TODO: implement me
    json_dir = input_data.get("raw_dir")
    avro_dir = input_data.get("stg_dir")

    if not json_dir:
        return {
            "message": "json_dir parameter missed",
        }, 400

    rewrite_to_dir(json_dir,avro_dir)

    return {
               "message": "Data processed successfully",
           }, 201


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8082)
