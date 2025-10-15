from pathlib import Path
from typing import Optional

from abspipeline import conf
from abspipeline.core.dt.entity import Entity
from abspipeline.libs import utils

from abspipeline.core import resolve


def find(search_type: str, filters: Optional[dict [str, str]] = None) -> list[Entity]:
    """
    For a given type and filter, return a list of Entity instances matching the filters

    Args:
        search_type: search type
        filters: dict of filter

    Returns:
        list of Entity instances

    """

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
        data = resolve.resolve(entity_type= search_type, path= path)
        if data is None:
            entities.append(Entity(type= search_type, data= data))

    return entities



if __name__ == "__main__":

    from pprint import pprint

    print("Main test starting...")

    search_type_input = find("asset_name", {"asset_type": 'Prop', "asset_name": "Model"})
    print(search_type_input)
    print("_" * 50)
    search_type_input = find("asset_name", {"asset_type": 'Prop'})
    pprint(search_type_input)
    print("_" * 50)
    search_type_input = find("asset_name")
    pprint(search_type_input)
    print("_" * 100)
    # path = Path("Asset/Character/Model")
    # search_type_input = resolve.resolve("asset_name", find("asset_name", {"asset_type": 'Prop'}))
    # #search_type_input = find("asset_name", resolve.resolve("asset_name", path) )
    # pprint(search_type_input)
