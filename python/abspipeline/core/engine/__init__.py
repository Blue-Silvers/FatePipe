import sys

def get(): # Todo: return type
    """
    Engine Factory. Returns the engine instance depending as context

    Returns:
        Engine

    """

    if "maya" in sys.executable:
        print("Use MayaEngine")
        from abspipeline.dcc.maya.engine.maya_engine import MayaEngine
        return MayaEngine()
    else:
        print("Use PythonEngine")
        from abspipeline.core.engine.python_engine import PythonEngine
        return PythonEngine()