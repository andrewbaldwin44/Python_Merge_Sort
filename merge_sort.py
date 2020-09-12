import random

def merge_sort(list):
    n = len(list)
    sorted = []

    if n <= 1:
        return list

    first_half = merge_sort(list[0:int(n/2)])
    second_half = merge_sort(list[int(n/2):])

    while first_half or second_half:
        if not second_half or (first_half and first_half[0] < second_half[0]):
            sorted.append(first_half.pop(0))
        elif second_half:
            sorted.append(second_half.pop(0))

    return sorted + first_half + second_half

print(merge_sort([6, 5, 4, 7, 9]))
print(merge_sort([6, 7, 45, 78, 72, 47, 103, 1675, 20, 43, 12, 4, 7009, 6, 5, 4, 3, 2, 1]))
print(merge_sort(["apple", "bear", "orange", "apricot", "applebees", "chicken"]))
print(merge_sort(["hello hi there", "hi"]))
print(merge_sort(["suzy sold sea shells down by the sea shore", "alex ate all apples", "peter piper piped pickles"]))

very_large_array = random.sample(range(0, 9999), 999)
print(merge_sort(very_large_array))
