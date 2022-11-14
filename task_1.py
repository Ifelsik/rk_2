"""task_1"""
def reverse(data):
    """Возвращает обратные числа"""
    number = data.split()
    reversed_numbers = []
    for num in number:
        reversed_numbers.append(1 / float(num))
    return tuple(reversed_numbers)
