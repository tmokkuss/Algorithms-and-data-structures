def more_than_five(lst):
    new_lst = []
    for i in lst:
        if i > 10:
            new_lst.append(i)
        else:
            continue
    return new_lst


if __name__ == '__main__':
    lst = [1, 5, 10, 11, 22, 33]
    print(more_than_five(lst=lst))