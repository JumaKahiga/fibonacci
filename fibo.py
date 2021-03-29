def fib(num):
    if num <= 1:
        return 1

    return fib(num - 1) + fib(num - 2)


def fib_list(arr: list):
    result = []
    for n in arr:
        result.append(fib(n))

    return result
