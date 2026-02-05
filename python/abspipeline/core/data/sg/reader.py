from abc import abstractmethod
from typing import Optional, Iterator

from abspipeline.core.dt.entity import Entity
from pathlib import Path
from abspipeline import conf
from abspipeline.libs import utils

from abspipeline.core import resolve

class SGReader():

    @abstractmethod
    def find(self, search_type: str, filters: Optional[dict [str, str]] = None)-> Iterator[Entity]:
        glob_expression = conf.templates.get(search_type).get("glob")

        keys = utils.get_pattern_keys(glob_expression)
        formatter = {key: "*" for key in keys}
        if filters:
            formatter.update(filters)

        glob_expression = glob_expression.format(**formatter)

        found = Path(conf.root).glob(glob_expression)
        print(f"search: {search_type}")

        entities = []
        for path in found:
            data = resolve.resolve(entity_type=search_type, path=path)
            if data:
                entities.append(Entity(type=search_type, data=data))

        return iter(entities)


    #def get(self, ):