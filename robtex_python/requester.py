"""Make and handle requests."""

import json

import requests


def get(api_path):
    """Request the api path and return the response."""
    response = requests.get(api_path)

    if response.ok:
        try:
            # return the json from the API endpoint
            return json.loads(response.text)
        except ValueError:
            # handle the list of dictionaries returned from the pdns endpoints
            return [json.loads(entry) for entry in response.text.split("\r\n") if entry != '']
    else:
        # print information about the error
        print("{} error retrieving {}: {}".format(response.status_code, api_path, response.text))
        return None
