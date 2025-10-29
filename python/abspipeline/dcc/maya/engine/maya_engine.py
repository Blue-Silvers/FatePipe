from pathlib import Path
from abspipeline.core.engine.python_engine import PythonEngine
import maya.cmds as cmds

class MayaEngine(PythonEngine):

    actions: list = ["open", "reference"]

    def open(self, path: Path) -> None:
        cmds.file(path, open=True, force=True)


if __name__ == "__main__":
    engine = MayaEngine()
    example = Path(
        "C:/Users/enzo.lahana/Documents/PycharmProjects/FatePipe/fileExplorer/Task/Asset/Prop/Model/v010/Work/Cloud_model-v001.mb")
    engine.open(example)
    # engine.explore(example)