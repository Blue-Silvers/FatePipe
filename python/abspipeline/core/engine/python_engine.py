from pathlib import  Path
import platform
import os
from abspipeline.core.engine.abstract_engine import AbstractEngine

class PythonEngine(AbstractEngine):
    actions: list = ["open","close"]

    def close(self, path: Path) -> None:
        print ("close")

    def open(self, path: Path) -> None:
        """
        open the given path

        Example
            >>> PythonEngine().open(Path(__file__))

        Args:
            path:

        Returns:

        """
        if platform.system() == "Windows":
            os.startfile(path)

    def explore(self, path: Path) -> None:
        """
        open the given path

        Example
            >>> PythonEngine().explore(Path(__file__))

        Args:
            path:

        Returns:

        """
        if platform.system() == "Windows":
            os.startfile(path.parent)