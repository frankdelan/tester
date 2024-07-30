def second_max(numbers: list[int]) -> tuple[int, int]:
    if numbers[0] > numbers[1]:
        first, second = numbers[0], numbers[1]
    else:
        first, second = numbers[1], numbers[0]

    for item in numbers:
        if item > first:
            second = first
            first = item
        elif first > item > second:
            second = item
    return first, second


print(second_max([1, 2, 5, 54, 123, 53, 76, -87, 12]))
print(second_max([7,6 ,32, 12]))
print(second_max([555, 51, 12, 75]))
