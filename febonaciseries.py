# def fib(n):    # write Fibonacci series up to n
#     print("Fibonacci series up to", n)
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()
# fib(200)

def fib2(n):  # return Fibonacci series up to n
    print("list containing the Fibonacci series up to", n)
    result = []
    a, b = 0, 1
    while a < n:
        # result.append(a)    # see below
        a, b = b, a+b
        result.append(a)
        return result
        # f100 = fib2(100)

fib2(
        