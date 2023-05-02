class Fibonacci:
    def fib_iterative(self, n):
        if n <= 1:
            return n

        prev, curr, count = 0, 1, 1
        while count < n:
            next = prev + curr
            prev = curr
            curr = next
            count += 1
        return curr

    def fib_recursive(self, n):
        # Stop criteria: when n = 0 or n = 1
        if n <= 1:
            return n
        else:
            return self.fib_recursive(n - 1) + self.fib_recursive(n - 2)
def main():
    solution = Fibonacci()
    r1 = solution.fib_iterative(7)
    r2 = solution.fib_recursive(7)
    print(r1, r2)

if __name__ == "__main__":
    main()