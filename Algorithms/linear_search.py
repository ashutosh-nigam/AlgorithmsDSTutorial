def linear_search(items_list: list, target: int):
    size = len(items_list)
    for i in range(0, size):
        if items_list[i] == target:
            return i
    return None


def verify(index: int, target: int):
    if index is None:
        print(f'Target item {target} no found')
    else:
        print(f'Target Item {target} found at Index: {index}')


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = linear_search(items, 6)
verify(result, 6)
