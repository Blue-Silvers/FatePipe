from abc import abstractmethod
from typing import Optional, Iterator

from abspipeline.core.dt.entity import Entity


class Reader():

    @abstractmethod
    def find(self, search_type: str, filters: Optional[dict [str, str]] = None)-> Iterator[Entity]:


        pass

    #def get(self, ):