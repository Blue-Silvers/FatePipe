name = "FatePipe"
version = "0.1.0"
requires = [
    'qtpy',
    'shotgun_api3',
    'pyside6'
]

tools = ["browser"]

def commands():
    env.PYTHONPATH.append('{root}/python')