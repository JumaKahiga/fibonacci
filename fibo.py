from concurrent.futures import ThreadPoolExecutor


def fib(num):
    if num <= 1:
        return 1

    return fib(num - 1) + fib(num - 2)


def fib_list(arr: list):
    result = []
    for n in arr:
        result.append(fib(n))

    return result


def fib_list_threading(arr: list):
    result = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        _result = executor.map(fib, arr)

    if not _result:
        return result

    return list(_result)
