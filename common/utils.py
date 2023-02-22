"""Util functions"""

import json
from typing import Any, List

import azure.functions as func


def documents_to_json(doc_list: func.DocumentList) -> List[Any]:
    """Convert a list of documents loaded from CosmosDB into a list of json objects
    """
    return [json.loads(doc.to_json()) for doc in doc_list]


def get_param(request: func.HttpRequest, key: str, default_value: Any = None) -> Any:
    """Takes a request and extracts the given parameter.

    Args:
        req: An HttpRequest object.
        key: A string of the parameter to extract.
        default_value: Return this when the param was not provided.
        check_bool_str: Check the param value as a string bool representation.
    """
    value = request.params.get(key)
    if not value:
        try:
            req_body = request.get_json()
            value = req_body.get(key)
        except ValueError:
            pass
        except AttributeError:
            pass
    return value if value is not None else default_value


def get_response(body: str, status_code=200) -> func.HttpResponse:
    """Get an HTTP response object for Functions

    Args:
        body (str): Response body string
        status_code (int, optional): Response status code. Defaults to 200.
    """
    return func.HttpResponse(body, status_code=status_code, headers={'Content-Type': 'application/json'})
