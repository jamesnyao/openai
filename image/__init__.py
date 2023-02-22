"""Entry point of the image function"""

import logging
import os

import azure.functions as func

import openai
from common import utils


def main(req: func.HttpRequest) -> func.HttpResponse:
    """NA
    Args:
        req: The http request
    Returns:
        A json formatted str of the response.
    """

    logging.info('Python HTTP trigger function.image')

    openai.api_key = os.getenv('OPENAI_API_KEY')
    prompt = utils.get_param(req, 'prompt', '')

    response = openai.Image.create(prompt=prompt, n=1, size='1024x1024')
    image_url = response['data'][0]['url']  # type: ignore

    return func.HttpResponse(f'<img src={image_url}>', status_code=200)
