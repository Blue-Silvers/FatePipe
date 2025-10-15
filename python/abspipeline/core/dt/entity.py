from dataclasses import dataclass

@dataclass(frozen=True)
class Entity:

    type: str
    data: dict[str, str]


if __name__ == "__main__":
    test = Entity(type="asset_name", data={"type": "Asset", "asset_type": "Character", "asset_name": "Model"})
    print(test)