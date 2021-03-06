def assert_dict(a, b):
    # to improve
    return a == b


def assert_list(a, b):
    # won't work with nested lists
    asserts = []
    assert len(a) == len(b)
    for index, item in enumerate(a):
        b_item = b[index]
        asserts.append(item == b_item and type(item) == type(b_item))
    return all(asserts)


def assert_float(a, b):
    return isinstance(a, float) and isinstance(b, float) and a == b


def assert_str(a, b):
    return isinstance(a, str) and isinstance(b, str) and a == b


def assert_none(a, b):
    return a is None and b is None


def assert_int(a, b):
    return isinstance(a, int) and isinstance(b, int) and a == b


def assert_bool(a, b):
    return isinstance(a, bool) and isinstance(b, bool) and a == b
