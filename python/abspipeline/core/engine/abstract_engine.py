from pathlib import  Path

class AbstractEngine:

    def open(self, path: Path) -> None:
        pass

    def explore(self, path: Path) -> None:
        pass

