from abspipeline.core.dt.entity import Entity
from typing import Any, Optional
from abspipeline.core.data.sg import connect

sg = connect.get_sg()


class SGWriter():

    def create(self, entity: Entity, data: Optional[dict [str, Any]] = None) -> bool:
        hardCodeData = {
            'project': {"type": "Project", "id": 1359},
            'code': 'Blue',
            'sg_status_list': 'ip'
        }

        if data is not None:
            hardCodeData.update(data)

        result = sg.create('Asset', hardCodeData)

        '''global sg

        if do_new:
            print("[sgtest] Creating new SG connection")
            return shotgun_api3.Shotgun(**credentials)

        if not sg:
            print("[sgtest] Creating SG connection")
            sg = shotgun_api3.Shotgun(**credentials)

        return sg

        sg.update(entity_type, found.get("id"), data)

        pass'''
        return result

    def update(self, entity: Entity, data: Optional[dict [str, Any]] = None) -> bool:
        pass