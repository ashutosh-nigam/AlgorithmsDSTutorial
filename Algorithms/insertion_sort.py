def insertion_sort(items: list):
    size = len(items)
    for i in range(1, size):
        temp = items[i]
        j = i - 1
        while items[j] > temp and j >= 0:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = temp
    return items


lst = [1, 5, 3, 4, 0, 8, 6]
insertion_sort(lst)
print(lst)
