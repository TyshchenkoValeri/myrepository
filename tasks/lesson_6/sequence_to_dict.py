def to_dict(lst: list):
    """
      Converting sequence to dictionary representation
    :param lst: list or tuple or string
    :return: dict
    """
    if not isinstance(lst, list):
        raise TypeError('parameter should to be list type only')
    res_dict = {}
    for element in lst:
        res_dict[element] = element
    return res_dict
