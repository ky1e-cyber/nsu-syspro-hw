from typing import Dict

def reverse_dict(hmap: Dict) -> Dict:
    """ Returns a reverse dictianary where keys are input dict values and vice-versa
    >>> reverse_dict({"Ivanov": 97832, "Petrov": 55521, "Kuznecov": 97832})
    {97832: ('Ivanov', 'Kuznecov'), 55521: 'Petrov'}

    >>> reverse_dict({(1, 2): 97, 1: 555, 2: 97, 3: 555})
    {97: ((1, 2), 2), 555: (1, 3)}
    """
    ret_hmap: Dict = dict()
    is_tuple: Dict = dict.fromkeys(hmap.values(), False)

    def _insert(key, value):
        if key in ret_hmap.keys():
            if is_tuple[key]:
                ret_hmap[key] = ret_hmap[key] + (value, )
            else:
                ret_hmap[key] = (ret_hmap[key], value)
                is_tuple[key] = True
        else:
            ret_hmap[key] = value

    for key, item in hmap.items():
        _insert(item, key)

    return ret_hmap

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    try: 
        reverse_dict({1: [2, 3]})
    except Exception as e:
        assert type(e) == TypeError
        print("TypeError test passed")

