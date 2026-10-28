def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False
    return True