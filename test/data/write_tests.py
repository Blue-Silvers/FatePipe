from abspipeline.core.dt.entity import Entity
from abspipeline.core.data.sg.writer import SGWriter

from pprint import pformat

entity = Entity(type = "asset_name",
                data={"asset_type" : "Character", "asset_name": "Blue"})

print("- - - Simple Create - - -")
print(f"About to create entity: {pformat(entity)}")

writer = SGWriter()
done = writer.create(entity)
print (done)


print("- - - Create with data - - -")
data = {'description':'Role of Fate', 'image':'C:/Users\enzo.lahana\Downloads\RoF.png'}

print(f"About to create entity: {pformat(entity)}")
print(f"With data: {pformat(data)}")


writer = SGWriter()
done = writer.create(entity, data=data)
print (done)