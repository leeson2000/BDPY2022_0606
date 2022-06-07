def func28(name, instructor, duration, *args):
    print(f"course name={name}, instructor={instructor}, duration={duration}")
    print(f"  開課時間是:{[t for t in args]}")


func28("BDPY", "Mark", 35)
func28("BDPY", "Mark", 35, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
func28("CPLUS", "Mark", 35, "Saturday")
