from pathlib import Path
from abspipeline import conf
print(conf.root)

def find(glob_template):

    glob_expression = conf.templates.get(glob_template).get("glob")
    found = Path(conf.root).glob(glob_expression)
    print(f"search: {glob_template}")
    return list(found)




#resolve(templates.get("asset_type").get("glob"),templates.get("asset_type").get("regex") )

if __name__ == "__main__":

    print("Main test starting...")
     # test glob
    glob_template = conf.templates.get("asset_type").get("glob")
    print(find(glob_template))

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
