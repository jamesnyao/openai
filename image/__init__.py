"""Entry point of the image function"""

import json
import logging
from datetime import datetime

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """ Gets the current availability state of the releasebot service.
    Args:
        req: The http request
    Returns:
        A json formatted str of the response.
    """

    logging.info('Python HTTP trigger function.image')

    return func.HttpResponse(json.dumps({'time': f'{datetime.now()}'}), status_code=200)
