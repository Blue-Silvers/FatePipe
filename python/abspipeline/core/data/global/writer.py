from abspipeline.core.data.writer import Writer
from abspipeline.core.data.sg.writer import SGWriter
from abspipeline.core.data.fs.writer import FSWriter

from abspipeline.core.dt.entity import Entity
from typing import Any, Optional

class GlobalWriter(Writer):

    def __init__(self):
        sg_writer = SGWriter()
        fs_writer = FSWriter()

    def create(self, entity: Entity, data: Optional[dict [str, Any]] = None) -> bool:

        self.sg_writer.create(entity, data)
        self.fs_writer.create(entity, data)

        pass

    def update(self, entity: Entity, data: Optional[dict [str, Any]] = None) -> bool:
        pass