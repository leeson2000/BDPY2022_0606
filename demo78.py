def fib(max):
    prev, curr = 0, 1
    count = 0
    while count < max:
        count += 1
        yield curr
        prev, curr = curr, curr + prev


print(list(fib(10)))
print(list(fib(20)))