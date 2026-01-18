from pathlib import Path
from abspipeline.core.engine.python_engine import PythonEngine
import maya.cmds as cmds

class MayaEngine(PythonEngine):

    actions: list = ["open", "reference", "save"]

    def open(self, path: Path) -> None:
        cmds.file(path, open=True, force=True)

    def reference(self, path: Path, namespace: str | None = None) -> None:
        if not namespace:
            namespace = path.stem  # ex: Cloud_model-v001

        cmds.file(
            str(path),
            reference=True,
            namespace=namespace,
            ignoreVersion=True,
            options="v=0"
        )


    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)

        cmds.file(rename=str(path))

        file_type = "mayaBinary" if path.suffix == ".mb" else "mayaAscii"

        cmds.file(save=True, type=file_type)


if __name__ == "__main__":
    engine = MayaEngine()
    example = Path(
        "C:/Users/enzo.lahana/Documents/PycharmProjects/FatePipe/fileExplorer/Task/Asset/Prop/Model/v010/Work/Cloud_model-v001.mb")
    engine.open(example)
    # engine.explore(example)