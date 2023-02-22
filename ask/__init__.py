"""Entry point of the ask function"""

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

    logging.info('Python HTTP trigger function.ask')

    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = utils.get_param(req, 'prompt', '')
    if prompt == '':
        return func.HttpResponse('Error: No prompt provided')
    # response = openai.Completion.create(model="text-davinci-003",
    #                                     prompt=prompt,
    #                                     temperature=0,
    #                                     max_tokens=100,
    #                                     top_p=1,
    #                                     frequency_penalty=0.0,
    #                                     presence_penalty=0.0,
    #                                     stop=["\n"])
    return func.HttpResponse('wip')
