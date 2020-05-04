def find_max(numbers):
    maxnum = numbers[0]
    for num in numbers:
        if num > maxnum:
            maxnum = num
    return maxnum