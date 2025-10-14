from pathlib import Path

templates = {
    "asset_type" : ".../fileExplorer/Task/Asset/Character",
    "asset_name" : "..."
}

found = Path("C:/").glob("Users/enzo.lahana/PycharmProjects/FatePipe")
print(list(found))

for f in found:
    print(f)