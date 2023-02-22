"""Entry point of the ping function"""

import json
import logging
from datetime import datetime

import azure.functions as func


def main(_req: func.HttpRequest) -> func.HttpResponse:
    """Gets the current availability state of the openai service.
    Args:
        req: The http request
    Returns:
        A json formatted str of the response.
    """

    logging.info('Python HTTP trigger function.ping')

    return func.HttpResponse(json.dumps({'utc_time': f'{datetime.utcnow()}'}), status_code=200)
