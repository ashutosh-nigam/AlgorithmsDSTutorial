def binary_search(items_list: list, target: int):
    first = 0
    last = len(items_list) - 1
    while first <= last:
        mid = (first + last) // 2
        if items_list[mid] == target:
            return mid
        elif items_list[mid] < target:
            first = mid + 1
        else:
            last = mid - 1
    return None


def verify(index: int, target: int):
    if index is None:
        print(f'Target item {target} not found')
    else:
        print(f'Target Item {target} found at Index: {index}')


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(items, 6)
verify(result, 6)
