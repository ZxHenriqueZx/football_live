def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

def input_filter(value, _type):
    try:
        _input = _type(input(value))
        return _input
    except ValueError:
        raise ValueError(f'Este valor não é do tipo: {_type}')
