#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Make and handle requests."""

import json

import requests


def get(api_path):
    """Request the api path and return the response."""
    response = requests.get(api_path)

    if response.ok:
        # return the json from the API endpoint
        return json.loads(response.text)
    else:
        # print information about the error
        print("{} error retrieving {}: {}".format(response.status_code,
                                                  api_path, response.text))
        return None
