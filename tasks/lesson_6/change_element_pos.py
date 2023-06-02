def change_list_element_position(lst: list):
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
        return lst
    return lst
