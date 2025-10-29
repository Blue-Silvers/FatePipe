from abspipeline.core import engine as e

engine = e.get()

print(type(engine))

print(engine.actions)

func = getattr(engine, "open") # == engin.open
print(func)