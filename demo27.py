import demo26_lib

print(demo26_lib.__name__)
print(demo26_lib.foo(1, 2))
print(demo26_lib.bar(3, 4))

# from demo26_lib import foo
# from demo26_lib import bar
from demo26_lib import foo, bar

print(foo(5, 6))
print(bar(7, 8))

from demo26_lib import foo as f1
from demo26_lib import bar as b1

print(f1(9, 10))
print(b1(11, 12))