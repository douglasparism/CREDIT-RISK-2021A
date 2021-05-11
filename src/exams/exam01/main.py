import json
from .utils import flat_dictionary
from fintools.settings import get_logger

logger = get_logger(name="__main__")


class Main(object):

    def __init__(self):
        logger.info("Main object initialized.")

    @staticmethod
    def flatten(filename):
        with open(filename, "r") as f:
            example = json.loads(f.read())
        return flat_dictionary(example)
