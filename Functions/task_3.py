def reverse_odd_elements(lst):
    odd_elements = lst[1::2]
    odd_elements.reverse()
    for i in range(1, len(lst), 2):
        lst[i] = odd_elements.pop(0)
    return lst


lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = reverse_odd_elements(lst=lst)
print(result)
