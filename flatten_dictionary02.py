
def flatten(dictionary, parent_key='', separator='_'):
    items = []
    for key, value in dictionary.items():
        new_key = parent_key + separator + key if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten(value, new_key, separator=separator).items())
        else:
            items.append((new_key, value))
    return dict(items)

print(flatten({'a': 1, 'c': {'a': 2, 'b': {'x': 5, 'y' : 10}}, 'd': [1, 2, 3]}))
