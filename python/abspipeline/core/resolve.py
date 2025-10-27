import re
from pathlib import Path

from abspipeline import conf

path = 'fileExplorer/Task/Asset/Character/Model/v010/Publish'
pattern = 'fileExplorer/Task/Asset/(?P<asset_type>.*)/(?P<asset_name>.*)/(?P<asset_task>.*)/(?P<asset_version>.*)'


def resolve (entity_type: str, path: Path) -> dict[str, str]:
    """
    resolve entity type

    Args:
        entity_type: entity type
        pathP: dict of path

    Returns:
        dict of string - string

    """

    pattern = conf.templates.get(entity_type).get("regex")
    path = path.as_posix()
    re_pattern = re.compile(pattern)
    match = re_pattern.search(str(path))
    res = {}

    if match:
        res = match.groupdict()

    return res

# if __name__ == "__main__":
#     entity_type = "asset_type"
#     path = Path("Asset/Character/Model")
#     result = resolve(entity_type, path)
#     print(result)
