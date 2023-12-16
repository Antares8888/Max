result = []


def divider(a, b):
    try:
        return a / b
    except ZeroDivisionError as error:
        print(error)
    except TypeError as error:
        print(error)
    except IndexError as error:
        print(error)


try:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
except TypeError as error:
    data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
    print(error)

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)