from .item import Item

def get_multi(
        data : Item, 
        single_value_name : str, 
        multi_value_name : str, 
        dict_name : str = "name") -> list[str]:
    result : list[str] = list()
    single_value : str = data.getByName(single_value_name)
    if single_value: result.append(single_value)
    multi_value : list[dict[str, any]] = data.getListByName(multi_value_name, list())
    curr : dict[str, any]
    for curr in multi_value:
        v : str = curr[dict_name] if dict_name in curr else None
        if v and not v in result: result.append(v)
    return result