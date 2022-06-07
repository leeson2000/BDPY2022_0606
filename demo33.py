def func33(name, instructor, duration):
    print(f"course name={name},講師={instructor}, 時數={duration}")


poop = {'name': "POOP", 'instructor': "Mark Ho", "duration": 35}
func33(**poop)
bdpy = {'name': "BDPY"}
func33(**bdpy, instructor='Mark', duration=24)
pykt = {'instructor': "Meng-Hang Ho"}
func33(**pykt, name="PYKT", duration=35)