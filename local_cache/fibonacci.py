from functools import lru_cache


class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < 0 or index > self.n - 1:
                raise IndexError

            return Fibonacci.fib(index)
        else:
            indices = index.indices(self.n)
            return [Fibonacci.fib(k) for k in range(*indices)]

    @staticmethod
    @lru_cache(2**16)
    def fib(n):
        if n < 2:
            return 1
        return Fibonacci.fib(n-2) + Fibonacci.fib(n-1)


fibonacci = Fibonacci(10)

# access elements via indices
print('Accessing Fibonacci sequence using []:')
print(fibonacci[0])
print(fibonacci[5])
print(fibonacci[8])

print('Accessing Fibonacci sequence using for loop:')
# using for loop
for index, f in enumerate(fibonacci):
    print(f'Fibonacci of {index+1} is {f}')