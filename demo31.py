def demo31(name, **description):
    print(f"course name={name}")
    for k, v in description.items():
        print(f"  [{k}]:{v}")


demo31("PYKT", tool="Tensorflow", level="Intermediate", instructor="Mark Ho")
courseInfo = dict(tool="Tensorflow", level="Intermediate", instructor="Mark Ho")
print(courseInfo)
demo31("PYKT", **courseInfo)