def demo29(name, **description):
    print(f"course name={name}")
    for k, v in description.items():
        print(f"  [{k}]:{v}")


demo29("POOP")
demo29("BDPY", instructor="Mark Ho")
demo29("PYKT", tool="Tensorflow", level="Intermediate")
