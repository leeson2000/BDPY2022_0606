from datetime import datetime

now = datetime.now()
print(now)
print(repr(now))
print([now])
print((now,))
print({now})
print({"k1": now})
print([str(now)])