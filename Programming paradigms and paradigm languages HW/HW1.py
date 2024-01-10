
def sort_list_imperative(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] < numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

numbers_list = [9, 5, 2, 7, 1, 3]
result = sort_list_imperative(numbers_list)
print(result)



def sort_list_declarative(numbers):
    return sorted(numbers, reverse=True)

numbers_list = [9, 5, 2, 7, 1, 3]
result = sort_list_declarative(numbers_list)
print(result)