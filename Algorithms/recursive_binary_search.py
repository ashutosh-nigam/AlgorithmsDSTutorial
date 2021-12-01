def recursive_binary_search(items_list: list, target: int):
    size = len(items_list)
    if size == 0:
        return False
    middle = size // 2
    if items_list[middle] == target:
        return True
    else:
        if items_list[middle] < target:
            return recursive_binary_search(items_list[middle + 1:], target)
        else:
            return recursive_binary_search(items_list[:middle - 1], target)


def verify(index: int, target: int):
    if index is False:
        print(f'Target item {target} not found')
    else:
        print(f'Target Item {target} found')


items = [1, 2, 3, 4, 5, 6, 7, 8, 9]
verify(recursive_binary_search(items, 6), 6)
