from pathlib import Path
from abspipeline import conf
from abspipeline.libs import utils


def find(glob_template, **filters):
    print(filters)

    glob_expression = conf.templates.get(glob_template).get("glob")
    print(glob_expression)


    keys = utils.get_pattern_keys(glob_expression)
    formatter = {key: "*" for key in keys}
    if filters:
        formatter.update(filters)

    glob_expression = glob_expression.format(**formatter)


    found = Path(conf.root).glob(glob_expression)
    print(f"search: {glob_template}")
    return list(found)




#resolve(templates.get("asset_type").get("glob"),templates.get("asset_type").get("regex") )

if __name__ == "__main__":

    print("Main test starting...")
     # test glob

    search_type_input ="asset_name"
    print(find("asset_name", filters={"asset_type": 'Prop', "asset_name": "Model"}))

    # search = "asset_type"
    # print(find(search))
    # search = "asset_name"
    # print(find(search, filters={"asset_type": "Prop", "asset_name": "Model"}))
    # print(find(search, filters={"asset_type": "Prop", "asset_name": "Texture"}))


    # glob_template = templates.get("asset_type").get("glob")
    # found = Path(root).glob(glob_template)
    # print(f"search: {glob_template}")
    #
    # for f in found:
    #     print(f)
    #
    #     glob_template = templates.get("asset_name").get("glob")
    #
    # # test glob
    # glob_template = templates.get("asset_type").get("glob")
    # print(find(glob_template))
    # glob_template = templates.get("asset_name").get("glob")
    # print(find(glob_template))

    entity = ("asset_name",
              {"type": "Asset",
               "asset_type": "Character",
               "asset_name": "Model"})

    print("_" * 50)
