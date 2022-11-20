from abc import ABC, abstractmethod


class IRateLimiter(ABC):

    @abstractmethod
    def grant_access(self):
        pass
