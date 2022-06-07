def func32(name, instructor, duration):
    print(f"course name={name},講師={instructor}, 時數={duration}")


func32("POOP", "Mark", 35)

bdpy_list = ["BDPY", "Mark Ho", 28]
func32(*bdpy_list)
pykt_tuple = ("PYKT", "Mark Ho")
func32(*pykt_tuple, 35)