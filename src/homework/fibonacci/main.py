from typing import List

from fintools.settings import get_logger
from fintools.utils import timeit, caching

logger = get_logger(name=__name__)


class Main:

    def __init__(self):
        logger.info("Main object initialized.")

    @caching
    def element(self, position: int) -> int:
        result = 1 if position <= 2 else self.element(position - 1) + self.element(position - 2)
        return 0 if position <= 0 else result

    @timeit(logger=logger)
    def sequence(self, length: int) -> List[int]:
        return [self.element(i) for i in range(0, length)]
